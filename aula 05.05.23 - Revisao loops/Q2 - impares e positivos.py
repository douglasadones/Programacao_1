"""Escreva um programa que lê uma quantidade indeterminada de números inteiros e
escreve todos os que forem ímpares positivos (use o ‘continue’. Considerar o valor 99 como fim da
entrada."""


impares_positivos = []

while True:
    num = int(input("Informe um número (99 para terminar): "))
    if num == 99:
        break
    if not (num % 2 != 0 and num > 0):
        continue  # Interrompe a interação atual e continua para o próxima interação.
    impares_positivos.append(num)

print(impares_positivos)
