from cassandra.cqlengine import columns
from cassandra.cqlengine.models import Model

class Utente(Model):
    __keyspace__ = "tinder"
    id = columns.Text(primary_key=True, required=True)
    nome = columns.Text(required=True)
    cognome = columns.Text(required=True)
    mail = columns.Text(required=True, custom_index=True)
    password = columns.Text(required=True)
    nascita = columns.Text(required=True)
    genere = columns.Boolean(required=True)
    interessi = columns.List(columns.Text(), required=True, custom_index=True)
    token = columns.Text(required=True, custom_index=True)
    admin = columns.Boolean(required=True, custom_index=True, default=False)
    likes = columns.List(columns.Text(), required=True, default=[])
    dislikes = columns.List(columns.Text(), required=True, default=[])


class Interesse(Model):
    __keyspace__ = 'tinder'
    id = columns.Text(primary_key=True, required=True)
    nome = columns.Text(required=True)