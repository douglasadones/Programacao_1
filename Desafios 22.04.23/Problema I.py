"""
Interceptando Informa¸c˜oes
A Spies Breaching Computers (SBC), uma agˆencia privada de espi˜oes digitais, est´a desenvolvendo um
novo dispositivo para intercepta¸c˜ao de informa¸c˜oes que, atrav´es de ondas eletromagn´eticas, permite a
espionagem mesmo sem contato f´ısico com o alvo.
O dispositivo tenta coletar informa¸c˜oes de um byte por vez, isto ´e, uma sequˆencia de 8 bits onde
cada um deles, naturalmente, pode ter valor 0 ou 1. Em determinadas situa¸c˜oes, devido a interferˆencias
de outros dispositivos, a leitura n˜ao pode ser feita com sucesso. Neste caso, o dispositivo retorna o
valor 9 para o bit correspondente, informando que n˜ao foi poss´ıvel efetuar a leitura.
De forma a automatizar o reconhecimento das informa¸c˜oes lidas, foi feita uma solicita¸c˜ao de um
programa que, a partir das informa¸c˜oes lidas pelo dispositivo, informe se todos os bits foram lidos com
sucesso ou n˜ao. Sua tarefa ´e escrever este programa.
Entrada
A entrada consiste de uma ´unica linha, contendo 8 n´umeros inteiros N1,N2,N3,N4,N5,N6,N7 e
N8, indicando os valores lidos pelo dispositivo (Ni ´e 0, 1 ou 9 para 1 ≤ i ≤ 8).
Sa´ıda
Imprima uma ´unica linha contendo a letra mai´uscula “S” caso todos os bits sejam lidos com sucesso;
caso contr´ario imprima uma ´unica linha contendo a letra mai´uscula “F”, correspondendo a uma falha.
"""

n = int((input()))
alterado = str(n)

if '9' in alterado:
    print('F')
else:
    print('S')
