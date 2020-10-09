"""
Pacote responsável por obter os dados transformados e enviá-los para um banco de dados
ou qualquer outro lugar
"""

from .models import Postgres
from decouple import config

DB_HOST = config('DB_HOST')
DB_NAME = config('DB_NAME')
DB_USER = config('DB_USER')
DB_PASSWORD = config('DB_PASSWORD')

def carregar_postgres(pedidos):
    postgres = Postgres(DB_HOST, DB_NAME, DB_USER, DB_PASSWORD)
    postgres.enviar_pedidos(pedidos)
