"""
    Pacote com a finalidade de extrair e filtrar os arquivos de uma fonte de dados
"""

from .models import Extrator, ListOrdersExtrator, Seletor


def resgatar_pedidos(data_inicio, data_fim):
    url_list_orders_mais = "https://abramais.myvtex.com/api/oms/pvt/orders/?orderBy=creationDate," \
                           "desc&f_creationDate=creationDate:%5B" + str(data_inicio) + \
                           "T03:00:00.000Z%20TO%20" + str(data_fim) + "T02:59:59" \
                                                                      ".999Z%5D&utc=-0200&per_page=100&page={}"
    url_get_order_mais = "https://abramais.myvtex.com/api/oms/pvt/orders/{}"
    headers_mais = {
        "X-VTEX-API-AppKey": "vtexappkey-abramais-NJFRFU",
        "X-VTEX-API-AppToken": "DNIRZLTQJHYUDUGLXNKRCXHKTVVEWXJPSPWTVSTWGFJWOINDTJIBIACFFXXEP"
                               "PUMYJCOYMPETOLWNLWKHRLNOHHRMQNXUPGRLXXFGYFGTDITPGSUAMWYDGXRBLCIZSKE",
        "Content-type": "application/json"
    }
    url_list_orders_casa = "https://abracasa.myvtex.com/api/oms/pvt/orders/?orderBy=creationDate," \
                           "desc&f_creationDate=creationDate:%5B" + str(data_inicio) + \
                           "T03:00:00.000Z%20TO%20" + str(data_fim) + "T02:59:59" \
                                                                      ".999Z%5D&utc=-0200&per_page=100&page={}"
    url_get_order_casa = "https://abramais.myvtex.com/api/oms/pvt/orders/{}"
    headers_casa = {
        "X-VTEX-API-AppKey": "vtexappkey-abracasa-ALPXOA",
        "X-VTEX-API-AppToken": "GPYPEPWLVPLINMRINWUNQFZBTWUZQVUUUJHAQUHEIQTIJCOIRRWKCMHBQWVHVXUZUQ"
                               "NDFQRTOQFZLQRRHLHZZKSIBGKUYZIKWUNTOLDAZCWMHHPZFDAJPUAKYFBZGXUO"
                               "PUMYJCOYMPETOLWNLWKHRLNOHHRMQNXUPGRLXXFGYFGTDITPGSUAMWYDGXRBLCIZSKE",
        "Content-type": "application/json"
    }

    # Abra mais

    # pegar todos os pedidos da api de list orders
    extrator_list_mais = ListOrdersExtrator(url_list_orders_mais, headers_mais)
    pedidos_mais = [pedidos_mais for pedidos_mais in extrator_list_mais]

    # filtrar os ids dos pedidos (cadabra e mais)
    seletor_mais = Seletor(pedidos_mais)
    ids_cadabra, ids_mais = seletor_mais.filtrar_ids_cadabra_mais()

    # pegar os pedidos (cadabra e mais) da api get orders
    extrator_get_mais = Extrator(url_get_order_mais, headers_mais)
    pedidos_cadabra = [extrator_get_mais.baixar_pagina(id_cadabra) for id_cadabra in ids_cadabra]
    pedidos_mais = [extrator_get_mais.baixar_pagina(id_mais) for id_mais in ids_mais]

    # Abra Casa

    # pegar todos os pedidos da api de list orders
    extrator_list_casa = ListOrdersExtrator(url_list_orders_casa, headers_casa)
    pedidos_casa = [pedidos_casa for pedidos_casa in extrator_list_casa]

    # filtrar os ids dos pedidos (casa)
    seletor_casa = Seletor(pedidos_casa)
    ids_casa = seletor_casa.filtrar_ids_casa()

    # pegar os pedidos (casa) da api get orders
    extrator_get_casa = Extrator(url_get_order_casa, headers_casa)
    pedidos_casa = [extrator_get_casa.baixar_pagina(id_casa) for id_casa in ids_casa]

    return pedidos_cadabra, pedidos_mais, pedidos_casa
