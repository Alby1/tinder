from uuid import UUID
from typing import Optional
from pydantic import BaseModel
from datetime import datetime

class Utente(BaseModel):
    id: Optional[UUID]
    nome: str = ""
    cognome: str = ""
    mail: str = ""
    password: str = ""
    nascita: int | str = ""
    interessi: list[str] = []
    genere: bool = False # vero = uomo; falso = donna
    token: Optional[str] = "empty"

    def nascita(self):
        if type(self.nascita) is str:
            self.nascita = (datetime.fromisoformat(self.nascita) - datetime.datetime(1970,1,1)).days


class Utente_edit(BaseModel):
    id: Optional[UUID]
    nome: Optional[str] = ""
    cognome: Optional[str] = ""
    mail: Optional[str] = ""
    password: Optional[str] = ""
    nascita: Optional[int] | Optional[str] = ""
    interessi: Optional[list[str]] = []
    genere: Optional[bool] = False # vero = uomo; falso = donna
    token: str = "empty"

class Interesse(BaseModel):
    id: Optional[UUID]
    nome: str