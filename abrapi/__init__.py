from . import extract, transform, load
from .models import Data
import time


def iniciar(dt_inicial, dt_final):
    """:param dt_inicial: Quantidade de dias anteriores que define o início do intervalo de datas
       :param dt_final: Quantidade de dias anteriores que define o fim do intervalo de datas
    """
    data = Data(dt_inicial, dt_final)

    def etl():
        pedidos = extract.resgatar_pedidos(data.selecionada, data.selecionada)
        if pedidos is not None:
            query = transform.transformar_postgresql(pedidos)
            load.enviar_postgresql(query)

    try:
        while data.final >= data.selecionada:
            print("[Extraindo]", data.selecionada)
            etl()
            data.passar_dia()
        return "Finalizado com sucesso!"
    except KeyboardInterrupt:
        print('Processo interrompido manualmente pelo usuário!')
