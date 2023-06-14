# Ao instanciar um objeto, um método transparente chamado "new" cria o objeto e só dps o init constrói.
from random import randint


class Produto:
    ano = 2023

    def __init__(self, codigo, nome, preco):
        self.codigo = codigo
        self.nome = nome
        self.preco = preco
        self.__estoque = 20

    def get_codigo(self):
        return self.codigo

    def get_nome(self):
        return self.nome

    @property  # Python entende que esse é o método get
    def preco(self):  # Já entende que quando digitado "p1.preco" já estará chamando esse método
        return self._preco  # Sem esse underline, seria gerado um erro pois o método chamaria o método infinitamente

    @preco.setter  # Python entende que esse é o método set
    def preco(self, valor):
        if not isinstance(valor, float):  # Só vai settar se o valor for float (é uma forma de tratar o dado)
            raise TypeError('Valor inválido!')
            return
        self._preco = valor

    def set_nome(self, valor):
        self.nome = valor

    @classmethod
    def get_ano(cls):  # Retorna apenas o atributo da classe e não o do objeto (cls = class)
        return cls.ano

    @classmethod
    def set_ano(cls, valor):  # Altera o valor da Classe e não o do objeto (cls = class)
        cls.ano = valor

    @staticmethod
    def gerar_codigo():
        cod = randint(100, 999)
        return cod

    def __del__(self):
        print(f'Apagando produto {self.nome}')  # Aqui não será apagado. Associação!
