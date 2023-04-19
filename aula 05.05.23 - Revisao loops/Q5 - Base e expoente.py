"""Faça um algoritmo que peça dois números – base e expoente – calcule e mostre o primeiro
número elevado ao segundo número. Não utilize a função de potência da linguagem."""

base = int(input("Informe a base: "))
expoente = int(input("Informe o expoente: "))
potencia = 1

for multiplicacoes in range(expoente):
    potencia *= base
print(potencia)
