ASTRA_DB_CLIENT_ID = 'vBTwDYbXyEGAayuPOhGyyTZS'
ASTRA_DB_CLIENT_SECRET = 'OFOwZnrEtl-jL7OH2aaIs4ONXsdRBUyiZDhQHBD98NQJujTpj5XbqJ5ap81TGW,ezBuYRgNUBs0h-8i+92Ddk734aOZSdiK,d.wlZOjoW1kgviKcZryrf3EC4jRf7L4u'
ASTRA_DB_TOKEN = 'AstraCS:vBTwDYbXyEGAayuPOhGyyTZS:bb6e60e1feda2b732e2b0facf8083364b9e070c381e282ec20a221f62984f8bb'

from cassandra.cluster import Cluster
from cassandra.auth import PlainTextAuthProvider
from cassandra.cqlengine.connection import register_connection, set_default_connection


def get_cluster():
    cloud_config = {
        'secure_connect_bundle': 'connect.zip'
    }

    auth_provider = PlainTextAuthProvider(ASTRA_DB_CLIENT_ID, ASTRA_DB_CLIENT_SECRET)
    cluster = Cluster(cloud=cloud_config, auth_provider=auth_provider)
    return cluster
    
def get_session():
    cluster = get_cluster()
    session = cluster.connect()
    register_connection(str(session), session=session)
    set_default_connection(str(session))
    return session

""" session = get_session()
row = session.execute("select release_version from system.local").one()
if row:
    print(row[0])
else:
    print("error") """