import crud
import db
import models

data = {
    "nome": "franco"
}


from cassandra.cqlengine.management import sync_table

session = db.get_session()
sync_table(models.Utente)

print(crud.create_entry(data))