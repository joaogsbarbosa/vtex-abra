"""
    Pacote com a finalidade de extrair e filtrar os arquivos de uma fonte de dados
"""

from .models import Extrator, ListOrdersExtrator, Seletor
from decouple import config


def resgatar_pedidos(data_inicio, data_fim):
    url_list_orders_abramais = "https://abramais.myvtex.com/api/oms/pvt/orders/?orderBy=creationDate," \
                               "desc&f_creationDate=creationDate:%5B" + str(data_inicio) + \
                               "T00:00:00.000Z%20TO%20" + str(data_fim) + "T23:59:59" \
                                                                          ".999Z%5D&utc=-0200&per_page=100&page={}"
    url_get_order_abramais = "https://abramais.myvtex.com/api/oms/pvt/orders/{}"
    headers_abramais = {
        "X-VTEX-API-AppKey": config('ABRAMAIS_APPKEY'),
        "X-VTEX-API-AppToken": config('ABRAMAIS_APPTOKEN'),
        "Content-type": "application/json"
    }
    url_list_orders_abracasa = "https://abracasa.myvtex.com/api/oms/pvt/orders/?orderBy=creationDate," \
                               "desc&f_creationDate=creationDate:%5B" + str(data_inicio) + \
                               "T00:00:00.000Z%20TO%20" + str(data_fim) + "T23:59:59" \
                                                                          ".999Z%5D&utc=-0200&per_page=100&page={}"
    url_get_order_abracasa = "https://abracasa.myvtex.com/api/oms/pvt/orders/{}"
    headers_abracasa = {
        "X-VTEX-API-AppKey": config('ABRACASA_APPKEY'),
        "X-VTEX-API-AppToken": config('ABRACASA_APPTOKEN'),
        "Content-type": "application/json"
    }

    # Abra mais

    # pegar todos os pedidos da api de list orders
    abramais_list_extrator = ListOrdersExtrator(url_list_orders_abramais, headers_abramais)
    pedidos_abramais = [pedidos for pedidos in abramais_list_extrator]

    # filtrar os ids dos pedidos
    ids_abramais = Seletor().filtrar_ids(pedidos_abramais)

    # pegar os pedidos na api get orders
    abramais_get_extrator = Extrator(url_get_order_abramais, headers_abramais)
    pedidos_abramais = [abramais_get_extrator.baixar_pagina(id_abramais) for id_abramais in ids_abramais]

    # Abra Casa

    # pegar todos os pedidos da api de list orders
    abracasa_list_extrator = ListOrdersExtrator(url_list_orders_abracasa, headers_abracasa)
    pedidos_abracasa = [pedidos for pedidos in abracasa_list_extrator]

    # filtrar os ids dos pedidos (casa)
    ids_abracasa = Seletor().filtrar_ids(pedidos_abracasa)

    # pegar os pedidos (casa) da api get orders
    abracasa_get_extrator = Extrator(url_get_order_abracasa, headers_abracasa)
    pedidos_abracasa = [abracasa_get_extrator.baixar_pagina(id_abracasa) for id_abracasa in ids_abracasa]

    return pedidos_abramais, pedidos_abracasa
