from typing import Union
import requests
from jsonpath_rw import jsonpath, parse


class Extrator:
    """Faz requisições e extrai os dados em todas as páginas"""

    def __init__(self, url, headers=None):
        self.url = url
        self.headers = headers

    def __iter__(self):
        """Iteração é apenas usada quando há paginação"""

        self.pagina_atual = 1
        return self

    def __next__(self):
        pagina_baixada = self.baixar_pagina(self.pagina_atual)
        if pagina_baixada is not None:
            self.pagina_atual += 1
            return pagina_baixada
        else:
            raise StopIteration

    def baixar_pagina(self, numero=1) -> Union[dict, list, None]:
        """Usado para baixar uma única página"""

        resposta = requests.get(self.url.format(numero), headers=self.headers)
        if resposta.status_code == 200 and resposta.json() != "":
            return resposta.json()
        else:
            return None


class Seletor:
    """Filtra os objetos json utilizando o JSONPath"""

    def __init__(self, json):
        self.json = json

    def filtrar_ids(self):
        pass

    def filtrar_ids_cadabra_mais(self):
        pass