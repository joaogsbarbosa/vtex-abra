"""
    Pacote com a finalidade de extrair e filtrar os arquivos de uma fonte de dados
"""

from .models import Extrator, ListOrdersExtrator, Seletor
from decouple import config

def resgatar_pedidos(data_inicio, data_fim):
    url_list_orders_mais = "https://abramais.myvtex.com/api/oms/pvt/orders/?orderBy=creationDate," \
                           "desc&f_creationDate=creationDate:%5B" + str(data_inicio) + \
                           "T00:00:00.000Z%20TO%20" + str(data_fim) + "T23:59:59" \
                                                                      ".999Z%5D&utc=-0200&per_page=100&page={}"
    url_get_order_mais = "https://abramais.myvtex.com/api/oms/pvt/orders/{}"
    headers_mais = {
        "X-VTEX-API-AppKey": config('ABRAMAIS_APPKEY'),
        "X-VTEX-API-AppToken": config('ABRAMAIS_APPTOKEN'),
        "Content-type": "application/json"
    }
    url_list_orders_casa = "https://abracasa.myvtex.com/api/oms/pvt/orders/?orderBy=creationDate," \
                           "desc&f_creationDate=creationDate:%5B" + str(data_inicio) + \
                           "T00:00:00.000Z%20TO%20" + str(data_fim) + "T23:59:59" \
                                                                      ".999Z%5D&utc=-0200&per_page=100&page={}"
    url_get_order_casa = "https://abracasa.myvtex.com/api/oms/pvt/orders/{}"
    headers_casa = {
        "X-VTEX-API-AppKey": config('ABRACASA_APPKEY'),
        "X-VTEX-API-AppToken": config('ABRACASA_APPTOKEN'),
        "Content-type": "application/json"
    }

    # Abra mais

    # pegar todos os pedidos da api de list orders
    abramais_list_extrator = ListOrdersExtrator(url_list_orders_mais, headers_mais)
    pedidos_mais = [pedidos for pedidos in abramais_list_extrator]

    # filtrar os ids dos pedidos (cadabra e mais)
    ids_cadabra, ids_mais = Seletor().filtrar_ids_cadabra_mais(pedidos_mais)

    # pegar os pedidos (cadabra e mais) da api get orders
    abramais_get_extrator = Extrator(url_get_order_mais, headers_mais)
    pedidos_cadabra = [abramais_get_extrator.baixar_pagina(id_cadabra) for id_cadabra in ids_cadabra]
    pedidos_mais = [abramais_get_extrator.baixar_pagina(id_mais) for id_mais in ids_mais]

    # Abra Casa

    # pegar todos os pedidos da api de list orders
    abracasa_list_extrator = ListOrdersExtrator(url_list_orders_casa, headers_casa)
    pedidos_casa = [pedidos for pedidos in abracasa_list_extrator]

    # filtrar os ids dos pedidos (casa)
    ids_casa = Seletor().filtrar_ids_casa(pedidos_casa)

    # pegar os pedidos (casa) da api get orders
    abracasa_get_extrator = Extrator(url_get_order_casa, headers_casa)
    pedidos_casa = [abracasa_get_extrator.baixar_pagina(id_casa) for id_casa in ids_casa]

    return pedidos_cadabra, pedidos_mais, pedidos_casa
