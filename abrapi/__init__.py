from . import models

def connect(host, database, user, password):
    return models.ApiToTable(host=host, database=database, user=user, password=password)
