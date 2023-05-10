from cassandra.cqlengine import columns
from cassandra.cqlengine.models import Model

class Utente(Model):
    __keyspace__ = "tinder"
    id = columns.Text(primary_key=True, required=True)
    nome = columns.Text()
    cognome = columns.Text()
    password = columns.Text()
    nascita = columns.Date()


class Altra(Model):
    __keyspace__ = "tinder"
    id = columns.Text(primary_key=True, required=True)
    a = columns.Text()
    b = columns.Text()
    c = columns.Text()