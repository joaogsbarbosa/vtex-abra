from datetime import datetime, timedelta, timezone


class Data:
    """Data no fuso horário UTC, o mesmo utilizado na API da VTEX
    """
    def __init__(self, dt_inicial, dt_final):
        """:param dt_inicial: Quantidade de dias anteriores que define o início do intervalo de datas
           :param dt_final: Quantidade de dias anteriores que define o fim do intervalo de datas
        """
        # Remove sinal negativo
        dt_inicial, dt_final = abs(dt_inicial), abs(dt_final)

        # Transforma em datas
        dt_inicial = self.hoje - timedelta(days=dt_inicial)
        dt_final = self.hoje - timedelta(days=dt_final)

        # Se data inicial for posterior à data inicial, então inverter
        if dt_inicial > dt_final:
            dt_inicial, dt_final = dt_final, dt_inicial

        # Cria variáveis de instância
        self.selecionada = dt_inicial
        self.final = dt_final

    @property
    def hoje(self):
        return datetime.now(tz=timezone.utc).date()

    def passar_dia(self):
        """Muda a data selecionada para o dia seguinte
        """
        self.selecionada += timedelta(days=1)
