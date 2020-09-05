import requests
from jsonpath_rw import jsonpath, parse

class Extrator:
    """
    Faz requisições e extrai os dados em todas as páginas
    """
    def __init__(self, url, headers):
        self.url = url
        self.headers = headers

    def __iter__(self):
        self.pagina_atual = 1
        return self.baixar_pagina(self.pagina_atual)

    def __next__(self):
        self.pagina_atual += 1
        pagina_baixada = self.baixar_pagina(self.pagina_atual)
        if pagina_baixada is not None:
            return pagina_baixada
        else:
            raise StopIteration

    def baixar_pagina(self, numero):
        resposta = requests.get(self.url.format(numero), headers=self.headers)
        if resposta.status_code == 200:
            return resposta.json()
        else:
            return None


class Seletor:
    """
    Filtra os objetos utilizando o JSONPath
    """
    def __init__(self, objeto, path):


    pass
