from . import extract, transform, load
from datetime import datetime, timedelta


def iniciar(data=datetime.now().date().strftime("%Y-%m-%d")):
    data = datetime.strptime(data, '%Y-%m-%d').date()
    try:
        while True:
            print("[Resgatando]", data.strftime("%Y-%m-%d"))
            pedidos = extract.resgatar_pedidos(data, data)
            if pedidos is not None:
                query = transform.transformar_postgresql(pedidos)
                load.enviar_postgresql(query)
            if datetime.now().date() > data:
                data += timedelta(days=1)
            # time.sleep(900)
    except KeyboardInterrupt:
        print('Interrompido!')
