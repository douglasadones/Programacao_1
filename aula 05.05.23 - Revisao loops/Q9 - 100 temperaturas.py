"""O Departamento Estadual de Meteorologia te contratou para desenvolver um programa
que leia um conjunto de 100 temperaturas, e informe ao final a menor e a maior temperaturas
informadas, bem como a média das temperaturas."""

from random import randint

CONJUNTO_DE_TEMPERATURAS = 100

lista_de_temperaturas = [randint(-90, 60) for c in range(CONJUNTO_DE_TEMPERATURAS)]  # Simulando os dados de entrada
maior_temp = lista_de_temperaturas[0]
menor_temp = lista_de_temperaturas[0]
soma_das_temp = 0

print(lista_de_temperaturas)

for c in lista_de_temperaturas:
    if c < menor_temp:  # Obtendo a Maior temperatura
        menor_temp = c
    if c > maior_temp:  # Obtendo a menor temperatura
        maior_temp = c
    soma_das_temp += c  # Soma total para cálculo posterior da média

print(f"A maior temperatura registrada foi: {maior_temp}° ")
print(f"A menor temperatura registrada foi: {menor_temp}° ")
print(f"A média das temperaturas registrada foi: {round((soma_das_temp / CONJUNTO_DE_TEMPERATURAS), 2)}° ")
