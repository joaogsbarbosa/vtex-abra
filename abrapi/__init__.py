from . import extract, transform, load
from datetime import datetime


def rodar():
    hoje = datetime.now().strftime("%Y-%m-%d")

    pedidos_cadabra, pedidos_mais, pedidos_casa = extract.resgatar_pedidos(hoje, hoje)

    pedidos_cadabra_query = transform.transformar(pedidos_cadabra)
    pedidos_mais_query = transform.transformar(pedidos_mais)
    pedidos_casa_query = transform.transformar(pedidos_casa)

    load.carregar_postgres(pedidos_cadabra_query)
    load.carregar_postgres(pedidos_mais_query)
    load.carregar_postgres(pedidos_casa_query)
