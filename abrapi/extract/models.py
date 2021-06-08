from typing import Union
import requests


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
        while True:
            try:
                resposta = requests.get(self.url.format(numero), headers=self.headers)
            except:
                print('Erro ao baixar, tentando novamente:', self.url.format(numero))
            else:
                break

        if resposta.status_code == 200 and resposta.json():
            return resposta.json()
        else:
            return None


class ListOrdersExtrator(Extrator):
    """Classe específica para extrair os dados da
    API List Orders da VTEX. Similar à classe Extrator.
    """

    def baixar_pagina(self, numero=1) -> Union[dict, list, None]:
        while True:
            try:
                resposta = requests.get(self.url.format(numero), headers=self.headers)
            except KeyboardInterrupt:
                print('Processo interrompido manualmente pelo usuário!')
            except:
                print('Erro ao baixar, tentando novamente:', self.url.format(numero))
            else:
                break
        if resposta.status_code == 200 and resposta.json()["list"]:
            return resposta.json()
        else:
            return None
