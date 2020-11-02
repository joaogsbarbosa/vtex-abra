"""
    Pacote com a finalidade de extrair e filtrar os arquivos de uma fonte de dados
"""

from .models import Extrator, ListOrdersExtrator
from decouple import config
from .functions import gerar_get_order, gerar_list_orders, gerar_headers, filtrar_ids


ABRAMAIS_APPKEY = config('ABRAMAIS_APPKEY')
ABRAMAIS_APPTOKEN = config('ABRAMAIS_APPTOKEN')
ABRACASA_APPKEY = config('ABRACASA_APPKEY')
ABRACASA_APPTOKEN = config('ABRACASA_APPTOKEN')


def resgatar_pedidos(data_inicio, data_fim):

    abramais_list = gerar_list_orders('abramais', data_inicio, data_fim)
    abramais_get = gerar_get_order('abramais')
    abramais_headers = gerar_headers(ABRAMAIS_APPKEY, ABRAMAIS_APPTOKEN)

    abracasa_list = gerar_list_orders('abracasa', data_inicio, data_fim)
    abracasa_get = gerar_get_order('abracasa')
    abracasa_headers = gerar_headers(ABRACASA_APPKEY, ABRACASA_APPTOKEN)

    # Abra Mais

    # Pegar todos os pedidos da api de list orders

    abramais_list_extrator = ListOrdersExtrator(abramais_list, abramais_headers)
    pedidos_abramais = [pedidos for pedidos in abramais_list_extrator]

    # Filtrar os ids dos pedidos
    ids_abramais = filtrar_ids(pedidos_abramais)

    # Pegar os pedidos na api get orders
    abramais_get_extrator = Extrator(abramais_get, abramais_headers)
    pedidos_abramais = [abramais_get_extrator.baixar_pagina(id_abramais) for id_abramais in ids_abramais]

    # Abra Casa

    # Pegar todos os pedidos da api de list orders
    abracasa_list_extrator = ListOrdersExtrator(abracasa_list, abracasa_headers)
    pedidos_abracasa = [pedidos for pedidos in abracasa_list_extrator]

    # Filtrar os ids dos pedidos
    ids_abracasa = filtrar_ids(pedidos_abracasa)

    # Pegar os pedidos da api get orders
    abracasa_get_extrator = Extrator(abracasa_get, abracasa_headers)
    pedidos_abracasa = [abracasa_get_extrator.baixar_pagina(id_abracasa) for id_abracasa in ids_abracasa]

    pedidos = []
    pedidos.extend(pedidos_abramais)
    pedidos.extend(pedidos_abracasa)

    if pedidos:
        return pedidos
    else:
        return None
