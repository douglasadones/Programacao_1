"""Crie um script que ler a temperatura de uma pessoa e mostre uma frase: “Febre Alta” (caso temperatura
seja maior ou igual a 39); “Febril” (caso temperatura esteja entre 39 e 37) ou “Sem Febre” (caso temperatura seja
menor do que 37)."""

temp = float(input(""))

if temp >= 39:
    print("Febre Alta")
elif 37 <= temp <= 39:
    print("Febril")
else:
    print("Sem Febre")
