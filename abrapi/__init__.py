from . import extract, transform, load
from .models import Data
import time


def iniciar(data=None):
    """:param data: String de data com formado AAAA-MM-DD
    """
    data = Data(data) if data else Data()
    try:
        while True:
            print("[Resgatando]", data.selecionada)
            pedidos = extract.resgatar_pedidos(data.selecionada, data.selecionada)
            if pedidos is not None:
                query = transform.transformar_postgresql(pedidos)
                load.enviar_postgresql(query)
            if data.hoje > data.selecionada:
                data.passar_dia()
            else:
                print("Aguardando 10 minutos...")
                time.sleep(600)
    except KeyboardInterrupt:
        print('Interrompido!')
