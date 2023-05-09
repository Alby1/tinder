from uuid import UUID
from typing import Optional
from pydantic import BaseModel

class Utente(BaseModel):
    id: UUID
    nome: Optional[str]
    cognome: Optional[str]
    password: Optional[str] # non opzional