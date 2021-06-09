from abrapi import iniciar
import sys


if __name__ == "__main__":
    if len(sys.argv) == 3:
        try:
            iniciar(int(sys.argv[1]), int(sys.argv[2]))
        except KeyboardInterrupt:
            print('Processo interrompido manualmente pelo usuário!')
    else:
        raise Exception("Requerido dois argumentos, consultar documentação.")
