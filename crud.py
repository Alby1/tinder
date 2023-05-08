import db
import models

import uuid
from cassandra.cqlengine.management import sync_table

session = db.get_session()
sync_table(models.Utente)

def create_entry(data: dict) -> models.Utente:
    data['id'] = str(uuid.uuid1())
    return models.Utente.create(**data)