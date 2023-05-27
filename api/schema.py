from uuid import UUID
from typing import Optional
from pydantic import BaseModel
from datetime import datetime

class Utente(BaseModel):
    id: Optional[UUID]
    nome: str = ""
    cognome: str = ""
    mail: str = ""
    password: str = None
    nascita: int | str = "" # anno-mese-giorno
    interessi: list[str] = []
    genere: bool # vero = uomo; falso = donna
    token: Optional[str] = "empty"
    admin: bool = False
    previously_matched: Optional[list[str]] = []
    likes: Optional[list[str]] = []
    dislikes: Optional[list[str]] = []

    def nascita_(self):
        if type(self.nascita_) is str:
            self.nascita = (datetime.fromisoformat(self.nascita) - datetime.datetime(1970,1,1)).days


class Utente_edit(BaseModel):
    id: Optional[UUID]
    nome: Optional[str] = ""
    cognome: Optional[str] = ""
    mail: Optional[str] = ""
    password: Optional[str] = ""
    nascita: Optional[int] | Optional[str] = ""
    interessi: Optional[list[str]] = []
    genere: Optional[bool] = None # vero = uomo; falso = donna
    token: str = "empty"
    admin: Optional[bool] = None
    likes: Optional[list[str]] = []
    dislikes: Optional[list[str]] = []

class Interesse(BaseModel):
    id: Optional[UUID]
    nome: str

class Interesse_edit(BaseModel):
    id: UUID
    nome: str