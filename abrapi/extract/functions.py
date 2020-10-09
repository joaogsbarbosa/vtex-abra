def gerar_list_orders(ambiente, data_inicio, data_fim):
    return "https://" + str(ambiente) + ".myvtex.com/api/oms/pvt/orders/?orderBy=creationDate," \
                                        "desc&f_creationDate=creationDate:%5B" + str(data_inicio) + \
           "T00:00:00.000Z%20TO%20" + str(data_fim) + "T23:59:59" \
                                                      ".999Z%5D&utc=-0200&per_page=100&page={}"


def gerar_get_order(ambiente):
    return "https://" + ambiente + ".myvtex.com/api/oms/pvt/orders/{}"


def gerar_headers(appkey, apptoken):
    return {
        "X-VTEX-API-AppKey": appkey,
        "X-VTEX-API-AppToken": apptoken,
        "Content-type": "application/json"
    }


def filtrar_ids(self, pedidos: list) -> list:
    """Filtra uma lista que contém os pedidos da API List Orders.
    Retorna uma lista contendo os ids dos pedidos.
    """

    ids = []
    for pagina in pedidos:
        for lista in pagina["list"]:
            ids.append(lista["orderId"])
    return ids
