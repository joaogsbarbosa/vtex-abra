from datetime import datetime, timedelta, timezone


class Data:
    """Data no fuso horário UTC, o mesmo utilizado na API da VTEX
    """
    def __init__(self, data=None):
        """:param data: String de data com formado AAAA-MM-DD
        """
        if data:
            self.selecionada = datetime.strptime(data, '%Y-%m-%d').date()
        else:
            self.selecionada = self.hoje

    @property
    def hoje(self):
        return datetime.now(tz=timezone.utc).date()

    def passar_dia(self):
        """Muda a data selecionada para o dia seguinte
        """
        self.selecionada += timedelta(days=1)
