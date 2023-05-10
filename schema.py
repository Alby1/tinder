from uuid import UUID
from typing import Optional
from pydantic import BaseModel

class Utente(BaseModel):
    id: Optional[UUID]
    nome: Optional[str]
    # non opzional ↓
    cognome: Optional[str]
    password: Optional[str]