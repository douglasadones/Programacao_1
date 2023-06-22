from historico import Historico


class Conta:
    def __init__(self, numero: int, saldo: float, titular: str):
        self.__numero = numero
        self.__saldo = saldo
        self.__titular = titular
        self.__historico = []

    @property
    def numero(self):
        return self.__numero

    @numero.setter
    def numero(self, valor):
        if isinstance(valor, int):
            self.__numero = valor

    @property
    def saldo(self):
        return self.__saldo

    @saldo.setter
    def saldo(self, valor):
        if isinstance(valor, float):
            self.__saldo = valor

    @property
    def titular(self):
        return self.__titular

    @titular.setter
    def titular(self, valor):
        if isinstance(valor, str):
            self.__titular = valor

    @property
    def historico(self):
        return self.__historico

    @historico.setter
    def historico(self, valor):
        if isinstance(valor, Historico):
            self.__historico = valor

    def adicionado_historico(self, operacao, valor):
        self.__historico.append(Historico(self.numero, valor, operacao))

    def mostrar_saldo(self) -> None:
        print()
        print("=" * 20)
        print(f"Saldo Atual: {self.__saldo}")
        print("=" * 20)
        print()

    def depositar(self, valor) -> bool:
        if isinstance(valor, float):
            self.__saldo += valor
            self.adicionado_historico(valor, "DE")
            return True
        else:
            print("Falha na Operação!")
            return False

    def sacar(self, valor):
        if valor <= self.__saldo:
            self.adicionado_historico(valor, "SA")
            self.__saldo -= valor
        else:
            print("Saldo insuficiente!")

    def transferir(self, conta1, conta2, valor: float):
        if conta1.saldo >= valor:
            self.adicionado_historico(valor, "TR")
            conta1.saldo -= valor
            conta2.saldo += valor
            # conta1.sacar(valor)  # Não usei isso para não bugar  o extrato final
            # conta2.depositar(valor)
        else:
            print("Falha na operação!")

    def extrato(self):
        for c in self.__historico:
            print("==========================")
            print(f"Número: {c.numero}")
            print(f"Operação: {c.operacao}")
            print(f"Valor: {c.valor}")
            print(f"Data: {c.data}")
        print("==========================")
        print()

