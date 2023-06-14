from random import randint


class ContaCorrente:
    def __init__(self, num: int, agencia: (int, float), titular: str, saldo: float):
        self.numero = num
        self.agencia = agencia
        self.titular = titular
        self.__saldo = saldo

    def sacar(self, valor) -> bool:
        if self.saldo >= valor:
            self.saldo -= valor
            return True
        else:
            return False

    def depositar(self, valor):
        self.saldo += valor

    def mostrar_saldo(self):
        print(f'Saldo Atual: R${self.saldo:.2f}')

    @staticmethod
    def gerar_numero():
        return randint(100, 999)

    @property
    def numero(self):
        return self._numero

    @numero.setter
    def numero(self, valor):
        if isinstance(valor, int):
            self._numero = valor

    @property
    def agencia(self):
        return self._agencia

    @agencia.setter
    def agencia(self, valor):
        if isinstance(valor, int):
            self._agencia = valor

    @property
    def titular(self):
        return self._titular

    @titular.setter
    def titular(self, valor):
        if isinstance(valor, int):
            self._titular = valor

    @property
    def saldo(self):
        return self._saldo

    @saldo.setter
    def saldo(self, valor):
        if isinstance(valor, int) or isinstance(valor, float):
            self._saldo = valor


cadastro = ContaCorrente(ContaCorrente.gerar_numero(), 154, 'Fernando', 1525.36)

