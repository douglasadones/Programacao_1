from agencia import Agencia


class Cliente(Agencia):
    def __init__(self, cpf: int, nome: str,  cidade: str, uf: str):
        super().__init__(cpf, nome, cidade, uf)

    def get_cpf(self):
        super().get_conta()
        return self.conta

    def set_cpf(self, valor):
        super().set_conta(valor)
        if isinstance(valor, int):
            self.conta = valor
