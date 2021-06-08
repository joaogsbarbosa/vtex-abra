"""
Pacote responsável por obter os dados filtrados e executar os modelos de manipulação de dados,
visando agrupar os dados e torná-los coerentes
"""
from .functions import filtrar, para_postgresql, para_mysql


def transformar_postgresql(pedidos):
    """Recebe uma lista de pedidos e retorna as queries necessárias para a próxima etapa
    """
    pedidos_filtrado = functions.filtrar(pedidos)
    insert_query = para_postgresql(pedidos_filtrado)
    return insert_query


def transformar_mysql(pedidos):
    """Recebe uma lista de pedidos e retorna as queries necessárias para a próxima etapa
    """
    pedidos_filtrado = functions.filtrar(pedidos)
    insert_query = para_mysql(pedidos_filtrado)
    return insert_query
