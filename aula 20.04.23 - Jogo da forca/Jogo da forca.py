from random import randint
quant_vidas_6 = """
(X)----------|
 |           
 |          
 |          
 |
 """

quant_vidas_5 = """
(X)----------|
 |           O
 |         
 |          
 |
"""

quant_vidas_4 = """
(X)----------|
 |           O
 |           |
 |          
 |
"""

quant_vidas_3 = """
(X)----------|
 |           O
 |          /|
 |          
 |
"""

quant_vidas_2 = """
(X)----------|
 |           O
 |          /|\\
 |          
 |
"""

quant_vidas_1 = """
(X)----------|
 |           O
 |          /|\\
 |          /
 |
"""

quant_vidas_0 = """
(X)----------|
 |           O
 |          /|\\
 |          / \\
 |
"""

grafico = [quant_vidas_0, quant_vidas_1, quant_vidas_2, quant_vidas_3, quant_vidas_4, quant_vidas_5, quant_vidas_6]

vidas = 6
game_over = False

banco_de_palavras = [['FRUTA', 'ABACATE', 'ABACAXI', 'ACEROLA', 'AMORA', 'BANANA', 'CACAU', 'CAQUI', 'CARAMBOLA'],
                     ['ANIMAL', 'MACACO', 'CACHORRO', 'GATO', 'COELHO', 'CAVALO', 'ALCE', 'URSO', 'AVESTRUZ'],
                     ]

# --------------- Escolhendo a dica e a palavra ---------------------
palavra_sorteada = banco_de_palavras[randint(0, len(banco_de_palavras) - 1)]
dica = palavra_sorteada[0]
palavra = palavra_sorteada[randint(1, len(palavra_sorteada) - 2)]


# --------------- Construindo a palavra anônima ---------------------- #
print(f"############ JOGO DA FORCA ############\nA dica é > {dica} <")

print(quant_vidas_6)

palavra_escondida = []
for caractere in palavra:
    palavra_escondida.append('_')
print(*palavra_escondida)

while not game_over:
    letra = input("Escolha uma letra: ").upper()
    print()
    if letra in palavra and letra not in palavra_escondida:
        for index, digito in enumerate(palavra):
            if digito == letra:
                palavra_escondida[index] = letra
        print(*palavra_escondida)
    else:
        if letra not in palavra_escondida:
            vidas -= 1
        print(f"Errado! Você ainda tem {vidas} tentativas")
        print(grafico[vidas])
    if vidas == 0:
        game_over = True
    if not ('_' in palavra_escondida):
        break

if game_over:
    print(f"Você perdeu! A palavra era: {palavra}")
else:
    print(f'Parabéns! você descobriu a palavra!')
