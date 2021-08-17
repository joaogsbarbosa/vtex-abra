from . import extract, transform, load
from .models import Data


def iniciar(dt_inicial, dt_final):
    """:param dt_inicial: Quantidade de dias anteriores que define o início do intervalo de datas
       :param dt_final: Quantidade de dias anteriores que define o fim do intervalo de datas
    """
    data = Data(dt_inicial, dt_final)

    def etl():
        pedidos = extract.resgatar_pedidos(data.selecionada, data.selecionada)
        # Transforma e envia ao banco apenas se existir pedido baixado
        if pedidos is not None:
            query = transform.transformar_mysql(pedidos)
            load.enviar_mysql(query)
        else:
            raise Exception('Nenhum driver banco de dados válido foi selecionado!')

    try:
        while data.final >= data.selecionada:
            print("[Extraindo]", data.selecionada)
            etl()
            data.passar_dia()
        return "Finalizado com sucesso!"
    except KeyboardInterrupt:
        print('Processo interrompido manualmente pelo usuário!')
