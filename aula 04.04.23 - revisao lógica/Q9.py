"""Lê um conjunto de números inteiros (+/-). A flag de parada é o valor 0(zero). Mostrar a quantidade de números
positivos que são pares."""

num = 1
quantidade = 0
while num:
    num = int(input())
    if num > 0 and num % 2 == 0:
        quantidade += 1
print(quantidade)
