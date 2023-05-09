import db
import models

import uuid

def create_entry(data: dict) -> models.Utente:
    data['id'] = str(uuid.uuid1())
    return models.Utente.create(**data)