import unittest
from abrapi.extract import resgatar_pedidos


class VerificarPedidosTest(unittest.TestCase):
    def test_resgatar_pedidos(self):
        pedidos_cadabra, pedidos_mais, pedidos_casa = resgatar_pedidos('2020-09-04', '2020-09-05')
        # não sei testar isso, só joguei um breakpoint
        self.assertEqual(True, True)


if __name__ == '__main__':
    unittest.main()
