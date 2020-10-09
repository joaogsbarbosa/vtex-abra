from . import extract, transform, load
from datetime import datetime


def rodar():
    hoje = datetime.now().strftime("%Y-%m-%d")

    pedidos_abramais, pedidos_abracasa = extract.resgatar_pedidos(str(hoje), str(hoje))

    abramais_query = transform.transformar_postgresql(pedidos_abramais)
    abracasa_query = transform.transformar_postgresql(pedidos_abracasa)

    load.enviar_postgresql(abramais_query)
    load.enviar_postgresql(abracasa_query)
