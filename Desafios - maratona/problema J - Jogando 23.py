"""
Jogando 23
Vinte e trˆes ´e um jogo de cartas simples, jogado por crian¸cas. Como o nome sugere, ele ´e uma varia¸c˜ao
do jogo vinte e um (blackjack em inglˆes), que ´e um dos jogos mais jogados em cassinos e sites de jogos.
O jogo utiliza um baralho de 52 cartas, com quatro naipes, cada naipe com 13 cartas (´as, 2, 3, 4,
5, 6, 7, 8, 9, 10, valete, dama e rei). Os naipes das cartas n˜ao s˜ao relevantes. As cartas com figuras
(valete, dama e rei) valem dez pontos, as cartas com n´umeros valem o seu n´umero em pontos (por
exemplo, a carta 4 vale quatro pontos) e o ´as vale um ponto.
Ganha o jogo o jogador que tiver o maior n´umero de pontos, desde que n˜ao exceda 23. Se um
jogador tem um n´umero de pontos maior do que 23 dizemos que o jogador estourou.
As regras do jogo s˜ao simples: a cada partida, inicialmente o baralho ´e embaralhado, as cartas s˜ao
colocadas em um monte e cada jogador recebe duas cartas do monte. Todas as cartas s˜ao distribu´ıdas
com a face para cima (todos os jogadores vˆeem as cartas de todos os jogadores). O passo seguinte,
chamado de rodada, ´e repetido enquanto houver jogadores ativos: uma carta ´e retirada do monte e
colocada na mesa com a face para cima. Essa carta, denominada carta comum, vale para todos os
jogadores. Se um jogador estourar, ele sai do jogo. Vence a partida o jogador que numa determinada
rodada somar 23 (somando suas duas cartas iniciais mais as cartas comuns), ou se o jogador for o ´unico
jogador ativo ao final da rodada. Note que pode haver mais de um vencedor (cujas cartas somam 23)
e que pode n˜ao haver vencedor em uma partida.
Jo˜ao e Maria est˜ao jogando vinte e trˆes. Os dois s˜ao os ´unicos jogadores, nenhum dos dois estourou
e nenhum dos dois tem 23 pontos. Al´em disso, a pontua¸c˜ao dos jogadores ´e tal que a pr´oxima carta
comum pode fazer com que a partida termine.
Dadas as cartas iniciais de Jo˜ao e Maria e as cartas comuns, determine qual ´e o valor da carta de
menor valor que deve ser retirada do monte na pr´oxima rodada para que Maria ven¸ca a partida.
Entrada
A primeira linha da entrada cont´em um inteiro N (1 ≤ N ≤ 8), o n´umero de rodadas do jogo at´e
o momento. Cada carta ´e descrita por um inteiro I (1 ≤ I ≤ 13). Note que as cartas com figuras
(valete, dama e rei) s˜ao representadas na entrada pelos valores 11, 12 e 13 e n˜ao por quantos pontos
elas valem. A segunda linha cont´em dois inteiros, descrevendo as duas cartas iniciais de Jo˜ao. A
terceira linha cont´em dois inteiros, descrevendo as duas cartas iniciais de Maria. A quarta e ´ultima
linha cont´em N inteiros, descrevendo as cartas comuns, na ordem em que s˜ao retiradas do monte.
Sa´ıda
Seu programa deve produzir uma ´unica linha, contendo um ´unico inteiro, o valor da carta de menor
valor que deve ser retirada do monte na pr´oxima rodada para Maria vencer a partida, ou -1 se n˜ao for
poss´ıvel Maria vencer a partida nessa pr´oxima rodada.
"""

# -------------------------------------- Cartas atualmente disponíveis ---------------------------------------------
dict = {'1': 4, '2': 4, '3': 4, '4': 4, '5': 4, '6': 4, '7': 4,  '8': 4, '9': 4, '10': 4, '11': 4, '12': 4, '13': 4}

# -------------------------------- Obtendo Dados ---------------------------------------
rodada = int(input())
while not(1 <= rodada <= 8):
    rodada = int(input())
cartas_joao = input().split()
while not(1 <= int(cartas_joao[0]) <= 13 and 1 <= int(cartas_joao[1]) <= 13):
    cartas_joao = input().split()
cartas_maria = input().split()
while not(1 <= int(cartas_maria[0]) <= 13 and 1 <= int(cartas_maria[1]) <= 13):
    cartas_maria = input().split()
cartas_comuns = input().split()

# --------------- Removendo as cartas usadas do baralho ---------------------------
for c in cartas_joao:
    dict[c] -= 1
for c in cartas_maria:
    dict[c] -= 1
for c in cartas_comuns:
    dict[c] -= 1

soma_maria = soma_joao = 0

lista_cartas_comuns = []

for c in cartas_comuns:  # Obtendo a soma total das cartas comuns
    lista_cartas_comuns.append(int(c))
sum_cart_comuns = sum(lista_cartas_comuns)

for c in cartas_maria:  # Somando todas as cartas da maria
    if int(c) > 10:
        soma_maria += int(10)
    else:
        soma_maria += int(c)
soma_maria += sum_cart_comuns

for c in cartas_joao:  # Somando todas as cartas do Joao
    if int(c) > 10:
        soma_joao += int(10)
    else:
        soma_joao += int(c)
soma_joao += sum_cart_comuns

# ------------------------------------ Tratando Vitória/Derrota --------------------------------------------

if (soma_maria < 23) and (soma_joao < soma_maria) or soma_maria == soma_joao:  # Caso da Maria ganhar ou empate
    comum_necessaria = str(23 - soma_maria)
    if dict[comum_necessaria] > 0:
        print(comum_necessaria)
    else:
        print(-1)
elif (soma_maria < 23) and (23 > soma_joao > soma_maria):  # Caso Joao perder ou impossibilidade de vitória
    comum_necessaria = str(24 - soma_joao)
    if dict[comum_necessaria] > 0:
        print(24 - soma_joao)
    elif dict[comum_necessaria] == 0:
        for k, v in dict.items():
            if int(k) + soma_maria > 23:  # Verifica se existe a possibilidade de ganhar
                print(-1)
                break
            elif v != 0 and soma_joao + int(k) > 23:  # Encontra a carta mais próxima para joão perder
                print(k)
                break
    else:
        print(-1)
else:
    print(-1)
