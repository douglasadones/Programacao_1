class Titular:
    def __init__(self, nome, endereco, cpf):
        self.nome = nome
        self.endereco = endereco
        self.__cpf = cpf

    # getters e setters...


class Conta:

    def __init__(self, num, agencia, saldo):
        self.numero = num
        self.agencia = agencia
        self.titular = None
        self.saldo = saldo

    @property
    def numero(self):
        return self._numero

    @property
    def agencia(self):
        return self._agencia

    @property
    def titular(self):
        return self._titular

    @property
    def saldo(self):
        return self._saldo

    @numero.setter
    def numero(self, valor):
        if isinstance(valor, int):
            self._numero = valor

    @agencia.setter
    def agencia(self, valor):
        if isinstance(valor, str):
            self._agencia = valor

    @titular.setter
    def titular(self, valor):
        if isinstance(valor, Titular):  # Note que agora estamos adicionando um objeto da classe Titular aqui
            self._titular = valor

    @saldo.setter
    def saldo(self, valor):
        if isinstance(valor, float):
            self._saldo = valor

    def sacar(self, valor):
        if valor <= self.saldo:
            self.saldo -= valor

    def depositar(self, valor):
        self.saldo += valor

    def mostrar_saldo(self):
        print(f'Numero: {self.numero}')
        print(f'Agencia: {self.agencia}')
        print(f'Titular: {self.titular.nome}')
        print(f'Saldo: {self.saldo}')
        print('=========================')


c1 = Conta(1, "Parnaíba", 500.0)
t1 = Titular('Ana', 'Parnaiba', 123456)
c1.titular = t1  # Associação!

print(c1)
print(t1)

c1.mostrar_saldo()

del c1  # t1 continua existindo pq estamos em uma associação! (Cada objeto está em um endereço de memória diferente)


