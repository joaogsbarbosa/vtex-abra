"""
Pacote responsável por obter os dados transformados e enviá-los para um banco de dados
ou qualquer outro lugar
"""
from .models import Mysql


def enviar_mysql(pedidos):
    mysql = Mysql()
    mysql.enviar_pedidos(pedidos)
