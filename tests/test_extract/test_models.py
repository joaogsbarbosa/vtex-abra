import unittest
from abrapi.extract.models import Extrator, ListOrdersExtrator, Seletor
from .exemplo_de_respostas import list_orders_uma_pagina, list_orders_uma_pagina_ids,\
    list_orders_uma_pagina_ids_abramais, list_orders_duas_paginas, list_orders_duas_paginas_ids, \
    list_orders_duas_paginas_ids_abramais, typicode_posts, typicode_posts_1


class ExtratorTeste(unittest.TestCase):

    def test_pagina_unica_objeto(self):
        extrator = Extrator('https://my-json-server.typicode.com/typicode/demo/posts/1')
        pagina = extrator.baixar_pagina()
        self.assertEqual(pagina, typicode_posts_1)

    def test_pagina_unica_lista(self):
        extrator = Extrator('https://my-json-server.typicode.com/typicode/demo/posts')
        pagina = extrator.baixar_pagina()
        self.assertEqual(pagina, typicode_posts)

    def test_com_paginacao(self):
        extrator = Extrator('https://my-json-server.typicode.com/typicode/demo/posts/{}')
        pagina = [pagina for pagina in extrator]
        self.assertEqual(pagina, typicode_posts)


class SeletorTeste(unittest.TestCase):

    def test_filtrar_ids_casa(self):
        filtrado = Seletor().filtrar_ids_casa(list_orders_uma_pagina)
        self.assertEqual(filtrado, list_orders_uma_pagina_ids)

    def test_filtrar_ids_casa_duas_paginas(self):
        filtrado = Seletor().filtrar_ids_casa(list_orders_duas_paginas)
        self.assertEqual(filtrado, list_orders_duas_paginas_ids)

    def test_filtrar_ids_cadabra_mais(self):
        filtrado = Seletor().filtrar_ids_cadabra_mais(list_orders_uma_pagina)
        self.assertEqual(filtrado, list_orders_uma_pagina_ids_abramais)

    def test_filtrar_ids_abramais_duas_paginas(self):
        filtrado = Seletor().filtrar_ids_cadabra_mais(list_orders_duas_paginas)
        self.assertEqual(filtrado, list_orders_duas_paginas_ids_abramais)


if __name__ == '__main__':
    unittest.main()
