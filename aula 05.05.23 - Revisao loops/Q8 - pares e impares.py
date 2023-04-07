"""Faça um programa que peça 10 números inteiros, calcule e mostre a quantidade de
números pares e a quantidade de números impares."""

total_de_num_pares = 0
total_de_num_impares = 0

for nums in range(10):
    num = int(input("Informe o número: "))
    if num % 2 == 0:
        total_de_num_pares += 1
    else:
        total_de_num_impares += 1

print(f"Total de números pares: {total_de_num_pares}\nTotal de números ímpares: {total_de_num_impares}")
