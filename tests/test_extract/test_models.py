import unittest
from abrapi.extract.models import Extrator, Seletor
from .exemplo_de_respostas import exemplo_get_order
from .exemplo_de_respostas import exemplo_list_orders


class ExtratorTeste(unittest.TestCase):

    def test_pagina_unica_objeto(self):
        valor_esperado = {
            "id": 1,
            "title": "Post 1"
        }
        extrator = Extrator('https://my-json-server.typicode.com/typicode/demo/posts/1')
        pagina = extrator.baixar_pagina()
        self.assertEqual(pagina, valor_esperado)

    def test_pagina_unica_lista(self):
        valor_esperado = [
            {
                "id": 1,
                "title": "Post 1"
            },
            {
                "id": 2,
                "title": "Post 2"
            },
            {
                "id": 3,
                "title": "Post 3"
            }
        ]
        extrator = Extrator('https://my-json-server.typicode.com/typicode/demo/posts')
        pagina = extrator.baixar_pagina()
        self.assertEqual(pagina, valor_esperado)

    def test_com_paginacao(self):
        valor_esperado = [
            {
                "id": 1,
                "title": "Post 1"
            },
            {
                "id": 2,
                "title": "Post 2"
            },
            {
                "id": 3,
                "title": "Post 3"
            }
        ]
        extrator = Extrator('https://my-json-server.typicode.com/typicode/demo/posts/{}')
        pagina = [pagina for pagina in extrator]
        self.assertEqual(pagina, valor_esperado)


class SeletorTeste(unittest.TestCase):

    def test_filtrar_ids(self):
        seletor = Seletor(exemplo_list_orders)
        filtrado = seletor.filtrar_ids()
        valor_esperado = ['v502559llux-01', 'v502556llux-01', 'v502553llux-01', 'v502550llux-01', 'v502547llux-01',
                          'v502544llux-01', 'v502541llux-01', 'v502538llux-01', 'SCP-880102018018-01',
                          'SCP-880091692043-01', 'SCP-880091058221-01', 'SCP-880090643370-01',
                          'SCP-880090622238-01', 'MNC-877730530419-01', 'SCP-876733475998-01']
        self.assertEqual(filtrado, valor_esperado)

    def test_filtrar_ids_cadabra_mais(self):
        seletor = Seletor(exemplo_list_orders)
        filtrado = seletor.filtrar_ids_cadabra_mais()
        valor_esperado = (['v502559llux-01', 'v502556llux-01', 'v502553llux-01', 'v502550llux-01', 'v502547llux-01',
                           'v502544llux-01', 'v502541llux-01', 'v502538llux-01', 'SCP-880102018018-01',
                           'SCP-880091692043-01', 'SCP-880091058221-01', 'SCP-880090643370-01',
                           'SCP-880090622238-01', 'MNC-877730530419-01'], ['SCP-876733475998-01'])
        self.assertEqual(filtrado, valor_esperado)



if __name__ == '__main__':
    unittest.main()
