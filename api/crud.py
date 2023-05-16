from .models import Model

from cassandra.cqlengine.models import Model

import uuid

def create_entry(data: dict, model: Model) -> Model:
    data['id'] = str(uuid.uuid1())
    print(data)
    return model.create(**data)