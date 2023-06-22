from datetime import date


class Historico:
    def __init__(self, numero: int, operacao: str, valor: float):
        self.__numero = numero
        self.__operacao = operacao
        self.__valor = valor
        self.__data = self.data_atual()

    @property
    def numero(self):
        return self.__numero

    @numero.setter
    def numero(self, valor):
        if isinstance(valor, int):
            self.__numero = valor

    @property
    def operacao(self):
        return self.__operacao

    @operacao.setter
    def operacao(self, valor):
        if isinstance(valor, str):
            self.__operacao = valor

    @property
    def valor(self):
        return self.__valor

    @valor.setter
    def valor(self, valor):
        if isinstance(valor, float):
            self.__valor = valor

    @property
    def data(self):
        return self.__data

    @data.setter
    def data(self, valor):
        if isinstance(valor, str):
            self.__data = valor

    @staticmethod
    def data_atual():
        ano = date.today().year
        mes = date.today().month
        dia = date.today().day
        return f"{dia:0>2}/{mes:0>2}/{ano}"
