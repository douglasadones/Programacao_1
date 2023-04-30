"""
Problema A
Achando os Mon´otonos N˜ao-Triviais Maximais
Neste problemas iremos lidar com sequˆencias de caracteres, muitas vezes chamadas de strings. Uma
sequˆencia ´e n˜ao-trivial se ela possui ao menos dois elementos.
Dada uma sequˆencia s, dizemos que um trecho si, . . . , sj ´e mon´otono se todos seus caracteres s˜ao
iguais, e dizemos que ela ´e maximal se este trecho n˜ao pode ser estendido `a esquerda e nem `a direita
sem perder a monotonicidade.
Dada uma sequˆencia composta apenas por caracteres “a” e “b”, determine quantos caracteres “a”
ocorrem em trechos mon´otonos maximais n˜ao-triviais.
Entrada
A entrada ´e composta por duas linhas. A primeira linha cont´em um ´unico inteiro N, satisfazendo
1 ≤ N ≤ 105. A segunda linha cont´em uma string, com exatamente N caracteres, composta apenas
pelos caracteres “a” e “b”.
Sa´ıda
A sa´ıda ´e composta por uma ´unica linha contendo um inteiro correspondente `a quantidade
"""

n = int(input())
string = input()
string += "b"

caractere_anterior = ""
quant_a_momentaneo = quant_a = 0

for caractere in range(len(string)):
    if string[caractere] == 'a':
        quant_a_momentaneo += 1
    elif string[caractere] == 'b' and quant_a_momentaneo <= 1:
        quant_a_momentaneo = 0
    elif string[caractere] == 'b' and quant_a_momentaneo > 1:
        quant_a += quant_a_momentaneo
        quant_a_momentaneo = 0

print(quant_a)


# Lendo um arquivo

file = open('A_25', 'r')
for linha in file:
    somatorio = cont = 0
    linha = linha.strip()
    for letra in linha:
        if letra == 'a':
            cont += 1
        elif cont > 1:
            somatorio += cont
            cont = 0
        elif cont == 1:
            cont = 0
    if cont > 1:
        somatorio += cont
    print(somatorio, end=' -> ')
    print(linha)
    file.close()
