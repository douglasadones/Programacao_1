"""Faça um programa que imprima o fatorial de um número. O valor de entrada deve ser
menor ou igual a 20."""

num = int(input("Informe um número (menor ou igual a 20): "))

if num <= 20:
    fatorial = 1
    for c in range(2, num + 1):
        fatorial *= c
    print(fatorial)
