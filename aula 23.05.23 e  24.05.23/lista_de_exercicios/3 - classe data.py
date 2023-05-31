from datetime import datetime


class Data:
    def __int__(self, dia, mes, ano):
        if 31 < dia < 1:
            dia = 'DD'
        self.dia_fornecido = dia
        if 12 < mes < 1:
            mes = 'MM'
        self.mes_fornecido = mes
        if len(ano) != 4:
            ano = 'AAAA'
        self.ano_fornecido = ano

    def __init__(self):
        self.dia = datetime.today().day
        self.mes = datetime.today().month
        self.ano = datetime.today().year

    def toString(self):
        pass
