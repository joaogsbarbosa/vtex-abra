from datetime import datetime
from datetime import timedelta
import abrapi


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
        print('interrupted!')


def abrir_menu():
    print("Escolhas as opções:")
    print("1 - resgatar pedidos a partir de hoje")
    print("2 - resgatar pedidos a partir de uma data definida")
    entrada = int(input())
    if entrada == 1:
        iniciar()
    elif entrada == 2:
        print("Digite a data inicial")
        print("ano-mês-dia")
        print("Ex: 2019-03-28")
        entrada = str(input())
        iniciar(entrada)
    else:
        abrir_menu()


if __name__ == "__main__":
    abrir_menu()
