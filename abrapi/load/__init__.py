"""
Pacote responsável por obter os dados transformados e enviá-los para um banco de dados
ou qualquer outro lugar
"""
from decouple import config
from .models import Postgresql, Mysql

DB_HOST = config('DB_HOST')
DB_NAME = config('DB_NAME')
DB_USER = config('DB_USER')
DB_PASSWORD = config('DB_PASSWORD')


def enviar_postgresql(pedidos):
    postgresql = Postgresql(DB_HOST, DB_NAME, DB_USER, DB_PASSWORD)
    postgresql.enviar_pedidos(pedidos)


def enviar_mysql(pedidos):
    mysql = Mysql(DB_HOST, DB_NAME, DB_USER, DB_PASSWORD)
    mysql.enviar_pedidos(pedidos)
