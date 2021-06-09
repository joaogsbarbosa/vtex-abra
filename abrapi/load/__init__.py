"""
Pacote responsável por obter os dados transformados e enviá-los para um banco de dados
ou qualquer outro lugar
"""
from .models import Postgresql, Mysql


def enviar_postgresql(pedidos):
    postgresql = Postgresql()
    postgresql.enviar_pedidos(pedidos)


def enviar_mysql(pedidos):
    mysql = Mysql()
    mysql.enviar_pedidos(pedidos)
