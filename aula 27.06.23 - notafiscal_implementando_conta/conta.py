from historico import Historico


class Conta:
    def __init__(self, numero: int, saldo: float, titular: str):
        self.__numero = numero
        self.__saldo = saldo
        self.__titular = titular
        self.__historico = []

    def get_numero(self):
        return self.__numero

    def set_numero(self, valor):
        if isinstance(valor, int):
            self.__numero = valor

    def get_saldo(self):
        return self.__saldo

    def set_saldo(self, valor):
        if isinstance(valor, float):
            self.__saldo = valor

    def get_titular(self):
        return self.__titular

    def set_titular(self, valor):
        if isinstance(valor, str):
            self.__titular = valor

    def get_historico(self):
        return self.__historico

    def set_historico(self, valor):
        if isinstance(valor, Historico):
            self.__historico = valor

    def adicionado_historico(self, operacao, valor):
        self.__historico.append(Historico(self.get_numero(), valor, operacao))

    def mostrar_saldo(self) -> None:
        print()
        print("=" * 20)
        print(f"Saldo Atual: {self.get_saldo()}")
        print("=" * 20)
        print()

    def depositar(self, valor) -> bool:
        if isinstance(valor, float):
            self.set_saldo(self.get_saldo() + valor)
            self.adicionado_historico(valor, "DE")
            return True
        else:
            print("Falha na Operação!")
            return False

    def sacar(self, valor) -> bool:
        if valor <= self.get_saldo():
            self.adicionado_historico(valor, "SA")
            self.set_saldo(self.get_saldo() - valor)
            return True
        else:
            return False

    def transferir(self, conta2, valor: float):
        self.adicionado_historico(-valor, "TR")
        conta2.adicionado_historico(valor, "TR")
        self.set_saldo(self.get_saldo() - valor)
        conta2.set_saldo(conta2.get_saldo() + valor)

    def extrato(self):
        for c in self.__historico:
            print("==========================")
            print(f"Número: {c.numero}")
            print(f"Operação: {c.operacao}")
            print(f"Valor: {c.valor:8.2f}")
            print(f"Data: {c.data}")
        print("==========================")
