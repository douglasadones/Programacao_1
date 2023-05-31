# Ao instanciar um objeto, um método transparente chamado "new" cria o objeto e só dps o init constrói.
from random import randint


class Produto:
    ano = 2023

    def __init__(self, codigo, nome, preco, estoque):
        self.codigo = codigo
        self.nome = nome
        self.preco = preco
        self.__estoque = estoque

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


p1 = Produto(1, 'mouse', 20.0, 10)
p2 = Produto(1, 'teclado', 60.0, 15)

Produto.ano = 2024
p1.ano = 2022  # Cria um atributo para o objeto, subistituindo o atributo da classe
print(Produto.__dict__)
print(p1.__dict__)
print(p2.__dict__)

print(Produto.get_ano())
print(Produto.get_ano())

p1 = Produto(Produto.gerar_codigo(), "cabo", 20.0, 10)
p1.codigo = '200'
p1.preco = 30.0  # setando - Automaticamente chama o método marcado com .setter
print(p1.gerar_codigo(), p1.get_nome(), p1.preco)

produtos = []

produtos.append(Produto(Produto.gerar_codigo(), 'mouse', 20.0, 10))
produtos.append(Produto(Produto.gerar_codigo(), 'teclado', 60.0, 20))

print()

for produto in produtos:
    print(f'Código: {produto.get_codigo()}')
    print(f'Nome..: {produto.get_nome()}')
    print(f'Preço.: {produto.preco}')  # Controlado via marcador
    print('------------------------------')

"""
Método de classe:
    basta marcar o método com "@classmethod"
    aqui, no lugar do self. aparece o cls. mas é apenas uma boa prática de programação.
    
Método Estático
    Método dentro da classe que nem é método de classe e nem é método do objeto
    
@property e @nomedoatributo.setter
    Essas marcações que servem como get_ e set_, respectivamente, são a saída qque o próprio python arrumou para
    proteger e obrigar um tipo específico de dado nas entradas de atributos.
    
    O que for como int, só aceitará um int e etc...
    
"""