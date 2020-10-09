from . import extract, transform, load
from datetime import datetime


def rodar():
    hoje = datetime.now().strftime("%Y-%m-%d")

    pedidos_abramais, pedidos_abracasa = extract.resgatar_pedidos(str(hoje), str(hoje))

    abramais_query = transform.transformar(pedidos_abramais)
    abracasa_query = transform.transformar(pedidos_abracasa)

    load.carregar_postgres(abramais_query)
    load.carregar_postgres(abracasa_query)
