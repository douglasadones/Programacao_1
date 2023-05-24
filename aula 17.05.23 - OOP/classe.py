# Os pilares da O.O.P
#   1 - *Abstração
#   2 - Polimorfismo
#   3 - Encapsulamento
#   4 - Herança


#     Classe
# + atrib1: int
# + atrib2: str
# - atrib3: float
# + mostrar1():int # Se adicionar o ":" é para especificar o tipo do retorno do método
# + mostrar2():None
# - mostrar1():str
# O "-" diz que aquilo só pode ser acessado pelo objeto; o " + é que pode ser usado em qualquer parte do programa
# Os atributos devem ser privados "__" antes do nome do atributo para privar
# Para que um método seja privado, basta adicionar "__" antes do nomel dele


# Métodos:
#   getters - Obtém um valor/atributo (mesmo que seja privado) -  Exemplo na linha 30
#   setters - Reconfigura um valor/atributo


class Pet:
    def __init__(self, cor, idade, cpf):
        self.__cor = cor
        self.__idade = idade
        self.__cpf = cpf  # Atributo privado

    def get_cpf(self):  # Mostra um atributo (Mesmo privado)
        return self.__cpf

    def get_cor(self):
        return self.__cor

    def get_idade(self):
        return self.__idade

    def set_cpf(self, cpf):
        self.__cpf = cpf

    def set_cor(self, cor):
        self.__cor = cor

    def set_idade(self, idade):
        self.__idade = idade


p1 = Pet('Caramelo', 2, 123456)  # instanciando a classe (Criar um objeto)
# print(f"P1: {p1.cor}")  # Isso não funciona pq o atributo é privado
p2 = Pet('Branco', 1, 3214)
# p1.__cpf = 222222  # Isso não pode ser alterado fora da classe pois está protegida.
print(f'P1: {p1.get_cpf()}')

p1.set_cor('Laranja')

pets = [p1, p2]


ptes_2 = []
for i in range(2):
    cor = input("Cor: ")
    idade = int(input('Idade: '))
    cpf = int(input('CPF: '))
    pets.append(Pet(cor, idade, cpf))

for pet in pets:
    print(f'P1[Cor]: {pet.get_cor()}')
    print(f'P1[Idade]: {pet.get_idade()}')
    print(f'P1[CPF]: {pet.get_cpf()}')
