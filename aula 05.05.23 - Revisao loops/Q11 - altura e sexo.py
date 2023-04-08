"""Tem‐se um conjunto de dados contendo a altura e o sexo (M ou F) de 15 pessoas. Faça
um programa que calcule e mostre: (1) a maior e a menor altura do grupo; (2) a media de altura das
mulheres; (3) o numero de homens; e (4) o sexo da pessoa mais alta."""

from random import randint

dados = [["M", 1.3], ["F", 1.6], ["M", 2.0], ["F", 1.8], ["M", 1.7], ["F", 1.5], ["M", 1.6], ["M", 1.6], ["F", 1.6],
         ["M", 1.84], ["F", 1.77], ["M", 1.42], ["F", 1.53], ["M", 1.88], ["F", 1.93]]

maior_altura = dados[0][1]
menor_altura = dados[0][1]
soma_total_altura_mulheres = 0
quantidade_mulheres = 0
quantidade_homens = 0
sexo_da_pessoa_mais_alta = ""

for pessoa in dados:
    if pessoa[1] > maior_altura:
        maior_altura = pessoa[1]
        sexo_da_pessoa_mais_alta = pessoa[0]
    if pessoa[1] < menor_altura:
        menor_altura = pessoa[1]
    if pessoa[0] == "M":
        quantidade_homens += 1
    else:
        quantidade_mulheres += 1
    if pessoa[0] == "F":
        soma_total_altura_mulheres += pessoa[1]

print(f"""Maior altura cadastrada: {maior_altura} m
Menor altura cadastrada: {menor_altura} m
Média de altura das mulheres: {round((soma_total_altura_mulheres / quantidade_mulheres), 2)} m
Quantidade de homens cadastrados: {quantidade_homens}
Sexo da pessoa mais alta cadastrada: {sexo_da_pessoa_mais_alta}""")
