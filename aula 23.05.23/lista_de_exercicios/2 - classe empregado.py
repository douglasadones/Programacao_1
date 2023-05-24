class Empregado:
    def __init__(self, nome, fone, salario):
        self.nome = nome
        self.fone = fone
        if salario < 0:
            salario = 0.0
        self.salario = salario

    def get_nome(self):
        return self.nome

    def get_fone(self):
        return self.fone

    def get_salario(self):
        return self.salario

    def set_nome(self, novo_nome):
        self.nome = novo_nome

    def set_fone(self, novo_fone):
        self.fone = novo_fone

    def set_salario(self, novo_salario):
        if novo_salario < 0:
            novo_salario = 0.0
        self.salario = novo_salario


empregado_1 = Empregado('Alberto', 86999999999, -1000)

empregado_2 = Empregado('Berto', 86955555555, 5000)

lista_empregados = [empregado_1, empregado_2]

for c in lista_empregados:
    print(f'Nome do funcionário: {c.get_nome()}')
    print(f'Fone: {c.get_fone()}')
    print(f'Salário Mensal: {c.get_salario()}')
    print()

empregado_1.set_fone(86922222222)
empregado_1.set_salario(1865.25)
empregado_1.set_nome("Alberto Certo")

for c in lista_empregados:
    print(f'Nome do funcionário: {c.get_nome()}')
    print(f'Fone: {c.get_fone()}')
    print(f'Salário Mensal: {c.get_salario()}')
    print()


for c in lista_empregados:
    salario_antigo = c.get_salario()
    salario_novo = salario_antigo + (salario_antigo * (10/100))
    c.set_salario(salario_novo)


print(f'Salário de {empregado_1.get_nome()} após 10% de aumento: R$ {empregado_1.get_salario():.2f}')
print(f'Salário de {empregado_2.get_nome()} após 10% de aumento: R$ {empregado_2.get_salario():.2f}')
