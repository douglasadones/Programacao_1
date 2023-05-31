class Fatura:
    def __init__(self, num, desc, quant, valor):
        self.num_do_item = num
        self.descricao = desc
        if quant < 0:
            quant = 0
        self.quant_comprada = quant
        if valor < 0:
            valor = 0.0
        self.preco_uni = valor

    def getTotalDaFatura(self):
        return self.quant_comprada * self.preco_uni

    def get_num_do_item(self):
        return self.num_do_item

    def get_descricao(self):
        return self.descricao

    def get_quant_comprada(self):
        return self.quant_comprada

    def get_preco_uni(self):
        return self.preco_uni

    def set_num_do_item(self, num):
        self.num_do_item = num

    def set_descricao(self, desc):
        self.descricao = desc

    def set_quant_comprada(self, quant):
        if quant < 0:
            quant = 0
        self.quant_comprada = quant

    def set_preco_uni(self, preco):
        if preco < 0:
            preco = 0.0
        self.preco_uni = preco


num = int(input('Informe o num: '))
nome = input('Informe o Nome: ')
quant = int(input('Informe a quantidade do produto: '))
valor = float(input('Informe o valor do produto: '))

feijao = Fatura(num, nome, quant, valor)


print(feijao.get_num_do_item())
feijao.set_num_do_item(2)
print(feijao.get_num_do_item())

print(feijao.get_descricao())
feijao.set_descricao('Feijão Verde')
print(feijao.get_descricao())

print(feijao.get_preco_uni())
feijao.set_preco_uni(25.75)
print(feijao.get_preco_uni())

print(feijao.get_quant_comprada())
feijao.set_quant_comprada(300)
print(feijao.get_quant_comprada())

print(feijao.getTotalDaFatura())


feijao.set_quant_comprada(-25)
print(feijao.get_quant_comprada())

feijao.set_preco_uni(-200)
print(feijao.get_preco_uni())
