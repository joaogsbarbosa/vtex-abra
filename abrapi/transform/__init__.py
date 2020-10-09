"""
Pacote responsável por obter os dados filtrados e executar os modelos de manipulação de dados,
visando agrupar os dados e torná-los coerentes
"""
from . import functions

def transformar(pedidos):
    """Recebe uma lista de pedidos e retorna as queries necessárias para a próxima etapa
    """
    pedidos_filtrado = functions.filtrar(pedidos)
    insert_query = functions.insert_query(pedidos_filtrado)
    return insert_query
