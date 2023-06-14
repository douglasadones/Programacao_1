from datetime import date
from random import randint
from produto import Produto
# Note que todos os métodos usam o atributo vindo da classe Produto. Exemplo de agregação.
# SOLID --> Pesquisar depois


class NotaFiscal:
    def __init__(self):
        self.numero = NotaFiscal.gerar_codigo()
        self.data = date.today()
        self.total = 0.00
        self.produtos = []

    def inserir_produto(self, produto):
        self.produtos.append(produto)

    def emitir_cupom(self):
        print("=" * 20)
        print("COD ITEM      PREÇO")
        print("-" * 20)
        for produto in self.produtos:
            print(f"{produto.codigo}", end=' ')
            print(f"{produto.nome}", end='')
            print(" " * (10 - len(produto.nome)), end='')
            print(f"{produto.preco:5.1f}")
        print("-" * 20)
        self.calcular_total()
        print(f'TOTAL: R$ {self.total}')
        print("=" * 20)

    def calcular_total(self):
        total = 0.00
        for produto in self.produtos:
            total += produto.preco
        self.total = total

    @staticmethod
    def gerar_codigo():
        n = randint(1000, 9999)
        return n

    def __del__(self):
        print(f'Apagando nf {self.numero}')

#
# if __name__ == '__main__':
#     nf = NotaFiscal()
#     print(nf.numero, nf.data, nf.total, nf.produtos)
#     nf.inserir_produto(Produto("mouse", 30.00))
#     nf.inserir_produto(Produto("teclado", 100.00))
#     nf.inserir_produto(Produto("ssd", 200.00))
#     print(nf.produtos[0].nome)
#
#     nf.emitir_cupom()
