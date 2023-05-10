from uuid import UUID
from typing import Optional
from pydantic import BaseModel
from datetime import datetime
from cassandra.cqlengine import columns

class Utente(BaseModel):
    id: Optional[UUID]
    # non opzional ↓
    nome: Optional[str] = ""
    cognome: Optional[str] = ""
    password: Optional[str] = ""
    nascita: Optional[str] = ""