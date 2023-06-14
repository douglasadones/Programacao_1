"""
Tentar fazer com 2 classes por associação

Data:
Numero:

N. / Produto / Qtd / Valor Unit / Valor Produto
1 / mouse    /  2  /     30     /     60
2 / teclado  /  1  /     65     /     65
3 / ssd      /  1  /    200     /    200
Valor Total: 325

"""


class Produto:
    def __init__(self, nome, val_unit):
        self.nome = nome
        self.valor_unitario = val_unit


class NotaFiscal:
    def __init__(self, data, num, quantidade):
        self.data = data
        self.numero = num
        self.quantidade = quantidade
