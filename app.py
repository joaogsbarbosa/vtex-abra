from abrapi import iniciar
import sys


def abrir_menu():
    s = "Escolhas as opções:\n1 - resgatar pedidos a partir de hoje\n2 - resgatar pedidos a partir de uma data " \
        "definida: "
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
    else:
        abrir_menu()
