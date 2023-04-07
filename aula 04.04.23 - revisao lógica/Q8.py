"""Crieum script que ler um número e exiba o dia correspondente da semana. (1 ‐
Domingo, 2 ‐ Segunda,..., 7 – Sábado), se digitar outro valor deve aparecer “valor inválido”."""
from builtins import list

list = ["Domingo", "Segunda", "Terça", "Quarta", "Quinta", "Sexta", "Sábado"]

num = int(input("")) - 1
if -1 < num < len(list):
    print(list[num])

# Ou
num = int(input(""))
if num == 1:
    print("Domingo")
elif num == 2:
    print("Segunda")
elif num == 3:
    print("Terça")
elif num == 4:
    print("Quarta")
elif num == 5:
    print("Quinta")
elif num == 6:
    print("Sexta")
elif num == 7:
    print("Sábado")
else:
    print("Valor Inválido")