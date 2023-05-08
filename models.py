from cassandra.cqlengine import columns
from cassandra.cqlengine.models import Model

class Utente(Model):
    __keyspace__ = "tinder"
    id = columns.Text(primary_key=True, required=True)
    nome = columns.Text(required=True)
    cognome: columns.Text(required=True)
    # password: columns.Text(required=True)