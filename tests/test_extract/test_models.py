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


class SeletorTeste:
    pass


if __name__ == '__main__':
    unittest.main()
