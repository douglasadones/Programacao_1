from conta import Conta


class Agencia:
    def __init__(self, nome: str, cidade: str, uf: str):
        self.conta = []
        self.numero =
        self.nome = nome
        self.endereco = []
        self.cidade = cidade
        self.uf = uf

    def get_conta(self):
        return self.conta

    def set_numero(self, valor):
        if isinstance(valor, int):
            self.numero.append(valor)

    def get_numero(self):
        return self.numero

    def get_nome(self):
        return self.nome

    def set_nome(self, valor):
        if isinstance(valor, str):
            self.nome = valor

    def get_endereco(self):
        return self.endereco

    def set_endereco(self, valor):
        if isinstance(valor, str):
            self.endereco.append(valor)

    def get_cidade(self):
        return self.cidade

    def set_cidade(self, valor):
        if isinstance(valor, str):
            self.cidade = valor

    def get_uf(self):
        return self.uf

    def set_uf(self, valor):
        if isinstance(valor, str):
            self.uf = valor
