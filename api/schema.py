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
    nascita: str = "" # anno-mese-giorno
    interessi: list[str] = []
    genere: bool # vero = uomo; falso = donna
    token: Optional[str] = "empty"
    admin: bool = False
    likes: Optional[list[str]] = []
    dislikes: Optional[list[str]] = []


class Utente_edit(BaseModel):
    id: Optional[UUID]
    nome: Optional[str] = ""
    cognome: Optional[str] = ""
    mail: Optional[str] = ""
    password: Optional[str] = ""
    nascita: Optional[str] = ""
    interessi: Optional[list[str]] = []
    genere: Optional[bool] = None # vero = uomo; falso = donna
    token: str = "empty"
    admin: Optional[bool] = None
    likes: Optional[list[str]] = []
    dislikes: Optional[list[str]] = []

class Utente_publicly_shareable(BaseModel):
    id: UUID
    nome: str = ""
    cognome: str = ""
    mail: str = ""
    password: str = None
    nascita: str = "" # anno-mese-giorno
    interessi: list[str] = []
    genere: bool # vero = uomo; falso = donna
    interessi_comuni: list[str] = []

class Interesse(BaseModel):
    id: Optional[UUID]
    nome: str

class Interesse_edit(BaseModel):
    id: UUID
    nome: str

class PropostaAppuntamento(BaseModel):
    id: Optional[UUID]
    data: str
    utente_chiedente: str
    utente_chieditore: str

class Appuntameto(BaseModel):
    id: Optional[UUID]
    data: str
    proposta: str