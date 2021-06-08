from abrapi import iniciar
import sys


if __name__ == "__main__":
    if len(sys.argv) == 3:
        iniciar(int(sys.argv[1]), int(sys.argv[2]))
    else:
        raise Exception("Requerido dois argumentos, consultar documentação.")
