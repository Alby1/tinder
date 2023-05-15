from fastapi import FastAPI, Response, status
from cassandra.cqlengine.management import sync_table, drop_table
from typing import List

import uvicorn
import bcrypt
import secrets

import db
import models
import schema
import crud

app = FastAPI()

@app.on_event("startup")
def startup():
    global session
    session = db.get_session()
    sync_table(models.Utente)
    sync_table(models.Interesse)


@app.get("/")
def root():
    return {"response": "hello world!"}

@app.post("/users/add", response_model=schema.Utente)
def user_add(data: schema.Utente):
    data.password = bcrypt.hashpw(data.password.encode('utf8'), bcrypt.gensalt()).decode('utf8')
    return crud.create_entry(dict(data), models.Utente)

@app.post("/users/edit")
def user_edit(response: Response, data: schema.Utente_edit):
    utente = session.execute("SELECT * FROM utente WHERE mail = %s ALLOW FILTERING", [data.mail]).one()
    try:
        data = dict(data)
        #print(data)
        for key in data.keys():
            if data[key] is not None and key != "mail":
                print(data[key])
                session.execute(f'UPDATE utente SET "{key}" = \'{data[key]}\' WHERE "id" = \'{utente["id"]}\'')
        return {"outcome" : "valid"}
    except Exception as e: print(e)
    response.status_code = status.HTTP_401_UNAUTHORIZED
    return {"outcome": "invalid"}

@app.get("/users", response_model=List[schema.Utente])
def get_users():
    return list(models.Utente.objects.all())

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


@app.get("/interests", response_model=List[schema.Interesse])
def get_interessi():
    return list(models.Interesse.objects.all())

@app.post("/interests/add", response_model=schema.Interesse)
def add_interess(data: schema.Utente):
    return crud.create_entry(dict(data), models.Interesse)

if __name__ == "__main__":
    uvicorn.run("main:app", reload=True, host="0.0.0.0", port=5000)