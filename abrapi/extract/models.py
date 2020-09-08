from typing import Union
import requests
from jsonpath_rw import jsonpath, parse


class Extrator:
    """Classe genérica que faz requisições a uma URL
    e extrai os dados em todas as páginas caso seja iterada
    ou em uma página com o método baixar página.
    Deverá conter {} no lugar do número da página para usar
    os recursos de paginação.
    """

    def __init__(self, url, headers=None):
        self.url = url
        self.headers = headers

    def __iter__(self):
        """Iteração genérica para percorrer e baixar páginas.
        Necessita que a URL contenha {}.
        """

        self.pagina_atual = 1
        return self

    def __next__(self):
        pagina_baixada = self.baixar_pagina(self.pagina_atual)
        if pagina_baixada:
            self.pagina_atual += 1
            return pagina_baixada
        else:
            raise StopIteration

    def baixar_pagina(self, numero=1) -> Union[dict, list, None]:
        """Usado para baixar uma única página"""

        resposta = requests.get(self.url.format(numero), headers=self.headers)
        if resposta.status_code == 200 and resposta.json():
            return resposta.json()
        else:
            return None


class ListOrdersExtrator(Extrator):
    """Classe específica para extrair os dados da
    API List Orders da VTEX. Similar à classe Extrator.
    """

    def baixar_pagina(self, numero=1) -> Union[dict, list, None]:
        resposta = requests.get(self.url.format(numero), headers=self.headers)
        if resposta.status_code == 200 and resposta.json()["list"]:
            return resposta.json()
        else:
            return None


class Seletor:
    """Filtra os objetos json utilizando o JSONPath"""

    def filtrar_ids_casa(self, pedidos: list) -> list:
        jsonpath_expr = parse('list[*].orderId')
        ids_casa = []
        for pagina in pedidos:
            ids_casa += [match.value for match in jsonpath_expr.find(pagina)]
        return ids_casa

    def filtrar_ids_cadabra_mais(self, pedidos: list) -> (list, list):
        jsonpath_expr = parse('list[*]')
        ids_cadabra, ids_mais = [], []
        for pagina in pedidos:
            pedidos = [match.value for match in jsonpath_expr.find(pagina)]
            for pedido in pedidos:
                if pedido["salesChannel"] == "1":
                    ids_cadabra.append(pedido["orderId"])
                else:
                    ids_mais.append(pedido["orderId"])
        return ids_cadabra, ids_mais
