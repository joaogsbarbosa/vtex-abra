from . import extract, transform, load


def rodar():
    pedidos_cadabra, pedidos_mais, pedidos_casa = extract.resgatar_pedidos('2020-09-04', '2020-09-05')

    pedidos_cadabra_query = transform.transformar(pedidos_cadabra)
    pedidos_mais_query = transform.transformar(pedidos_mais)
    pedidos_casa_query = transform.transformar(pedidos_casa)

    load.carregar_postgres(pedidos_cadabra_query)
    load.carregar_postgres(pedidos_mais_query)
    load.carregar_postgres(pedidos_casa_query)

