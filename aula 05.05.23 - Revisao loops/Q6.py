"""Faça um programa que peça 5 valores positivos do usuário (usando while). Caso o usuário
digite algum número negativo o programa deve terminar imediatamente. Caso termine normalmente
informe que os dados foram inseridos com sucesso (use o else)."""

acumulador_de_num = 0
num_negativo = False
while True:
    if acumulador_de_num == 5:
        break
    num = int(input("Informe os número positivos: "))
    if num < 0:
        num_negativo = True
        break
    acumulador_de_num += 1
if num_negativo:
    pass
else:
    print("Os dados foram inseridos com sucesso")