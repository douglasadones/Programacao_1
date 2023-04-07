"""Faça um programa que identifica os 15 primeiros números primos (utilizando a instrução
break)."""

acumulador_de_numeros = 2
total_de_numeros_primos = 1
print("Os 15 primeiros números primos são: \n1")

while True:
    primo = True

    for c in range(2, acumulador_de_numeros):
        if acumulador_de_numeros % c == 0:
            primo = False
            break

    if primo:
        print(acumulador_de_numeros)
        total_de_numeros_primos += 1

    if total_de_numeros_primos >= 15:
        break
    acumulador_de_numeros += 1
