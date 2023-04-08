"""Uma fábrica tem 10 representantes. Cada um recebe uma comissão calculada a partir do
número de itens de um pedido, segundo os seguintes critérios: (1) para até 19 itens vendidos, a
comissão é de 10% do valor total do pedido; (2) para pedidos de 20 e 49 itens, a comissão é de 15%
do valor total do pedido; (3) para pedidos de 50 a 74 itens, a comissão é de 20% do valor total do
pedido; e (4) para pedidos iguais ou superiores, a 75 itens a comissão é de 25%. Faça um programa
que lê a quantidade de itens de pedidos de cada representante e imprime o percentual de comissão
de cada um."""

representante_e_comissao = []

for representante in range(10):
    pedidos = int(input("Informe a quantidade de pedidos: "))
    if pedidos <= 19:
        comissao = 10
    elif 20 <= pedidos <= 49:
        comissao = 15
    elif 50 <= pedidos <= 74:
        comissao = 20
    else:
        comissao = 25
    representante_e_comissao.extend([[pedidos, comissao]])

for c in representante_e_comissao:
    print(f"Representante {representante_e_comissao.index(c) + 1}: \nItens: {c[0]}\nComissão: {c[1]}%\n")
