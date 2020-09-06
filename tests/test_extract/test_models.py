import unittest
from abrapi.extract.models import Extrator, Seletor


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

    def test_get_order(self):
        from .exemplo_de_respostas import exemplo_get_order
        seletor = Seletor(exemplo_get_order)
        filtrado = seletor.get_order()
        self.assertEqual(filtrado[0], exemplo_get_order)

    def test_list_orders(self):
        from .exemplo_de_respostas import exemplo_list_orders
        seletor = Seletor(exemplo_list_orders)
        filtrado = seletor.get_order()
        self.assertEqual(filtrado[0], exemplo_list_orders)


if __name__ == '__main__':
    unittest.main()
