"""
Pacote responsável por obter os dados transformados e enviá-los para um banco de dados
ou qualquer outro lugar
"""

from .models import Postgres


def carregar_postgres(pedidos):
    postgres = Postgres('ec2-3-229-210-93.compute-1.amazonaws.com', 'ddbgk544cdc7hh', 'sregkbahnbyhll',
                        '0d8cb2969d6cb7ab0be12e988b978abe0a5ac681d5e27964198b7fe656ddb40b')
    postgres.enviar_pedidos(pedidos)
