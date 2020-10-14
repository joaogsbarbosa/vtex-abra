from . import extract, transform, load
from datetime import datetime


def rodar(data: datetime = datetime.now()):
    data = data.strftime("%Y-%m-%d")

    pedidos_abramais, pedidos_abracasa = extract.resgatar_pedidos(data, data)

    abramais_query = transform.transformar_postgresql(pedidos_abramais)
    abracasa_query = transform.transformar_postgresql(pedidos_abracasa)

    load.enviar_postgresql(abramais_query)
    load.enviar_postgresql(abracasa_query)
