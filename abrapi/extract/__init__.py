"""
    Pacote com a finalidade de extrair e filtrar os arquivos de uma fonte de dados
"""

from .models import Extrator, Seletor


def requisitar(url, headers, api):
    """
    :param url: Deverá receber a URL, substituindo o número da
    página por {}
    :param headers: cabeçalho da requisição
    :param api: 'get_order' ou 'list_orders'
    """
    extrator = Extrator(url, headers)
    resposta = [resposta for resposta in extrator]
    seletor = Seletor(resposta)

    if api == 'get_order':
        return seletor.get_order()
    elif api == 'list_orders':
        return seletor.list_orders()
    else:
        return None
