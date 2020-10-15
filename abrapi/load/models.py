import psycopg2


class Postgresql:
    def __init__(self, host, database, user, password):
        self.conexao = psycopg2.connect(host=host, dbname=database, user=user, password=password)
        self.cursor = self.conexao.cursor()

    def enviar_pedidos(self, pedidos):
        for pedido in pedidos:
            self.cursor.execute(pedido)
        self.conexao.commit()
        print("Pedidos enviados ao banco!")
