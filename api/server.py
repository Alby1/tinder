from fastapi import FastAPI, Response, status
from cassandra.cqlengine.management import sync_table, drop_table
from typing import List, Optional

import bcrypt
import secrets

from .db import get_session
from .models import Interesse, Utente 
from .schema import Utente as Utente_, Interesse as Interesse_, Utente_edit, Interesse_edit, Utente_publicly_shareable
from .crud import create_entry

app = FastAPI()

@app.on_event("startup")
def startup():
    global session
    session = get_session()
    sync_table(Utente)
    sync_table(Interesse)


@app.get("/")
def root():
    return {"response": "hello world!"}

@app.post("/users/add", response_model=Utente_)
def user_add(data: Utente_):
    data.password = bcrypt.hashpw(data.password.encode('utf8'), bcrypt.gensalt()).decode('utf8')
    data.nascita_()
    data.admin = False
    return create_entry(dict(data), Utente)

@app.post("/users/edit")
def user_edit(response: Response, data: Utente_edit):
    utente = session.execute('SELECT * FROM utente WHERE "token" = %s ALLOW FILTERING', [data.token]).one()
    try:
        data = dict(data)
        for key in data.keys():
            if (data[key] is not None and data[key] != '' and data[key] != []) and (key != "token" and key != "admin"):
                d = f"{data[key]}" if type(data[key]) in [list, bool] else f"'{data[key]}'"
                session.execute(f'UPDATE utente SET "{key}" = {d} WHERE "id" = \'{utente["id"]}\'')
        return {"outcome" : "valid"}
    except Exception as e: print(e)
    response.status_code = status.HTTP_401_UNAUTHORIZED
    return {"outcome": "invalid"}

@app.get("/users", response_model=Optional[List[Utente_]])
def get_users(response: Response, token: str):
    utente: Utente = session.execute('SELECT * FROM utente WHERE "token" = %s ALLOW FILTERING', [token]).one()
    if utente:
        if utente['admin']:
            return list(Utente.objects.all())
    response.status_code = status.HTTP_401_UNAUTHORIZED
    return None

@app.get("/users/auth", response_model=dict)
def auth(response: Response, mail: str, password: str):
    utente = session.execute("SELECT * FROM utente WHERE mail = %s ALLOW FILTERING", [mail]).one()
    try:
        if bcrypt.checkpw(password.encode('utf8'), utente['password'].encode('utf8')):
            if utente['token'] == "empty":
                utente['token'] = secrets.token_hex(40)
                
                session.execute('UPDATE utente SET "token" = %s WHERE "id" = %s', [utente['token'], utente['id']])
            return {"outcome": "valid", "token": utente['token']}
    except: pass
    response.status_code = status.HTTP_401_UNAUTHORIZED
    return {"outcome" : "invalid"}

@app.get("/users/checkauth", response_model=dict)
def checkauth(response: Response, mail: str, token: str):
    utente = session.execute("SELECT * FROM utente WHERE mail = %s ALLOW FILTERING", [mail]).one()
    try:
        if utente['token'] == token:
            return {"outcome" : "valid"}
    except: pass
    response.status_code = status.HTTP_401_UNAUTHORIZED
    return {"outcome" : "invalid"}

@app.delete("/users", response_model=dict)
def delete_users(token: str, response: Response):
    utente: Utente = session.execute('SELECT * FROM utente WHERE "token" = %s ALLOW FILTERING', [token]).one()
    if utente:
        if utente['admin']:
            session.execute("truncate utente")
    response.status_code = status.HTTP_401_UNAUTHORIZED
    return None


@app.get("/interests", response_model=List[Interesse_])
def get_interessi():
    return list(Interesse.objects.all())

@app.post("/interests/add", response_model=Interesse_)
def add_interesse(data: Interesse_, token: str, response: Response):
    utente: Utente = session.execute('SELECT * FROM utente WHERE "token" = %s ALLOW FILTERING', [token]).one()
    if utente:
        if utente['admin']:
            return create_entry(dict(data), Interesse)
    response.status_code = status.HTTP_401_UNAUTHORIZED
    return None

@app.post("/interests/edit")
def edit_interesse(data: Interesse_edit, token:str, response: Response):
    utente: Utente = session.execute('SELECT * FROM utente WHERE "token" = %s ALLOW FILTERING', [token]).one()
    if utente:
        if utente['admin']:
            data = dict(data)
            for key in data.keys():
                if (data[key] is not None and data[key] != '' and data[key] != []) and (key != "id"):
                    d = f"{data[key]}" if type(data[key]) in [list, bool] else f"'{data[key]}'"
                    session.execute(f'UPDATE interesse SET "{key}" = {d} WHERE "id" = \'{data["id"]}\'')
            return {"outcome": "valid"}
    response.status_code = status.HTTP_401_UNAUTHORIZED
    return {"outcome": "invalid"}


@app.get("/users/match", response_model=Utente_publicly_shareable)
async def match_users(token: str, response: Response):
    utente: Utente = session.execute('SELECT * FROM utente WHERE "token" = %s ALLOW FILTERING', [token]).one()
    altri = session.execute(f'select * from utente').all()
    disponibili = []
    for a in altri:
        if a['id'] != utente['id']:
            interessi_comuni = set(a['interessi']).intersection(set(utente['interessi']))
            if len(interessi_comuni) > 0:
                if not (a['id'] in utente['likes'] or a['id'] in utente['dislikes']):
                    a['interessi_comuni'] = interessi_comuni
                    disponibili.append(a)

    disponibili = set(disponibili)
    return disponibili

@app.get("/users/like")
def like_user(token: str, altro: str, likes: bool, response: Response):
    utente: list = session.execute(f'SELECT {("likes" if likes else "dislikes")} FROM utente WHERE "token" = {token} ALLOW FILTERING').one()
    if not utente:
        response.status_code = status.HTTP_404_NOT_FOUND
        return {"outcome": "invalid"}
    
    utente.append(altro)
    session.execute(f'UPDATE utente SET {("likes" if likes else "dislikes")} = {utente} WHERE "token" = {token}')
    return {"outcome": "valid"}
        

@app.post("/users/grantadmin")
def user_grant_admin(token: str, altro: str, admin: bool, response: Response):
    utente: Utente = session.execute('SELECT * FROM utente WHERE "token" = %s ALLOW FILTERING', [token]).one()
    
    if utente:
        if utente['admin']:
                    session.execute(f'UPDATE interesse SET "admin" = {admin} WHERE "id" = \'{altro}\'')
                    return {"outcome": "valid"}
            
    response.status_code = status.HTTP_401_UNAUTHORIZED
    return {"outcome": "invalid"}