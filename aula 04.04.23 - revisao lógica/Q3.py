"""Crie um script que recebe a distância (em quilômetros) e o tempo de viagem (em
horas) de um automóvel, e mostrar se a velocidade media foi superior ao limite de
velocidade ou não (adote 110 km/h como velocidade máxima)."""

distancia = float(input(""))
tempo = int(input(""))

if distancia/tempo > 110:
    print("Velocidade média superior a permitida")
else:
    print("Velocidade média segura")
