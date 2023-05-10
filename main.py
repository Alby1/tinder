from fastapi import FastAPI
from cassandra.cqlengine.management import sync_table
from typing import List

import uvicorn
import json
import bcrypt

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


@app.get("/")
def root():
    return {"response": "hello world!"}

@app.get("/test", response_model=List[schema.Utente])
def test():
    return list(models.Utente.objects.all())

@app.get("/users/add", response_model=schema.Utente)
def user_add(data: schema.Utente):
    data.password = bcrypt.hashpw(data.password.encode('utf8'), bcrypt.gensalt())
    return crud.create_entry(data, models.Utente)
    return "ciao"


if __name__ == "__main__":
    uvicorn.run("main:app", reload=True, host="0.0.0.0", port=5000)