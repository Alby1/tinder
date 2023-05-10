import db
import models

from cassandra.cqlengine.models import Model

import uuid

def create_entry(data: dict, model: Model) -> models.Utente:
    data.id = str(uuid.uuid1())
    return model.create(**data)