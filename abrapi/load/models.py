import psycopg2
import mysql.connector
from decouple import config

DB_HOST = config('DB_HOST')
DB_NAME = config('DB_NAME')
DB_USER = config('DB_USER')
DB_PASSWORD = config('DB_PASSWORD')


class Postgresql:
    def __init__(self):
        self.conectar()

    def conectar(self):
        # Repete até 10 vezes caso haja algum erro na conexão com o banco de dados
        for tentativa in range(10):
            try:
                self.conexao = psycopg2.connect(host=DB_HOST, dbname=DB_NAME, user=DB_USER, password=DB_PASSWORD)
                self.cursor = self.conexao.cursor()
            except:
                print("Ocorreu um erro ao tentar se conectar ao banco de dados, tentando novamente.")
            else:
                break
        # Caso todas as 10 tentativas tenham falhado, tenta pela última vez
        else:
            print("Ultima tentativa de conexão com o banco de dados...")
            self.conexao = psycopg2.connect(host=DB_HOST, dbname=DB_NAME, user=DB_USER, password=DB_PASSWORD)
            self.cursor = self.conexao.cursor()

    def reconectar(self):
        self.conexao.close()
        del self.conexao, self.cursor
        self.conectar()

    def enviar_pedidos(self, pedidos):
        for pedido in pedidos:
            # Repete até 10 vezes caso haja algum erro na instrução SQL que faz o insert dos dados
            for tentativa in range(10):
                try:
                    self.cursor.execute(pedido)
                    self.conexao.commit()
                except Exception as e:
                    print("Ocorreu um erro ao executar uma instrução SQL ou dar commit, tentando novamente.")
                    print("Detalhes do erro:", e)
                    self.reconectar()
                else:
                    break
            # Caso todas as outras tentativas dê erro, tenta pela última vez e lança uma excessão
            else:
                print("Última tentativa....")
                self.reconectar()


class Mysql:
    def __init__(self):
        self.conectar()

    def conectar(self):
        # Repete até 10 vezes caso haja algum erro na conexão com o banco de dados
        for tentativa in range(10):
            try:
                self.conexao = mysql.connector.connect(host=DB_HOST, database=DB_NAME, user=DB_USER,
                                                       password=DB_PASSWORD)
                self.cursor = self.conexao.cursor()
            except:
                print("Ocorreu um erro ao tentar se conectar ao banco de dados, tentando novamente.")
            else:
                break
        # Caso todas as 10 tentativas tenham falhado, tenta pela última vez
        else:
            print("Ultima tentativa de conexão com o banco de dados...")
            self.conexao = mysql.connector.connect(host=DB_HOST, database=DB_NAME, user=DB_USER,
                                                   password=DB_PASSWORD)
            self.cursor = self.conexao.cursor()

    def reconectar(self):
        self.conexao.close()
        del self.conexao, self.cursor
        self.conectar()

    def enviar_pedidos(self, pedidos):
        for pedido in pedidos:
            # Repete 10 vezes caso haja algum erro na instrução SQL que faz o insert dos dados
            for tentativa in range(10):
                try:
                    self.cursor.execute(pedido)
                    self.conexao.commit()
                except Exception as e:
                    print("Ocorreu um erro ao executar uma instrução SQL ou dar commit, tentando novamente.")
                    print("Detalhes do erro:", e)
                    self.reconectar()
                else:
                    break
            else:
                # Caso todas as outras tentativas dê erro, tenta pela última vez e lança uma excessão
                print("Última tentativa....")
                self.reconectar()
