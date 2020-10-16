from datetime import datetime
from datetime import timedelta
import abrapi, sys


def iniciar(data=datetime.now().date()):
    if isinstance(data, str):
        data = datetime.strptime(data, '%Y-%m-%d').date()
    try:
        while True:
            print("Resgatando pedidos da data", data.strftime("%Y-%m-%d"))
            abrapi.rodar(data)
            if datetime.now().date() > data:
                data += timedelta(days=1)
    except KeyboardInterrupt:
        print('Interrompido!')


def abrir_menu():
    s = "Escolhas as opções:\n1 - resgatar pedidos a partir de hoje\n2 - resgatar pedidos a partir de uma data definida: "
    entrada = input(s)
    while entrada < "1" or entrada > "2":
        entrada = input(s)
    if entrada == "1":
        iniciar()
    elif entrada == "2":
        entrada = input("Digite a data inicial - dd/mm/aaaa: ")
        vdata = entrada.split("/")
        for (i, x) in enumerate(vdata):
            vdata[i] = x.strip()
        iniciar(vdata[2] + "-" + vdata[1] + "-" + vdata[0])


if __name__ == "__main__":
    if len(sys.argv) > 1:
        iniciar(sys.argv[1])
    abrir_menu()
