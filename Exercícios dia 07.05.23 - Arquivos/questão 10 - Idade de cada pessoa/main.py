"""Dado um arquivo contendo um conjunto de nome de pessoas e data de nascimento (DD MM
AAAA, isto é 3 inteiros seguidos), construir outro arquivo contendo os nomes e a idade de
cada pessoas. O programa deve ler o nome do arquivo a ser lido e carregar a data atual do
sistema."""
from datetime import date

dia_atual = date.today().day
mes_atual = date.today().month
ano_atual = date.today().year

arquivo = input('Informe o nome do arquivo: ')
existe = False

try:
    file = open(arquivo, 'r')
    file.close()
    existe = True
except:
    print('Arquivo não encontrado!')

if existe:
    with open('saida_teste', 'w') as saida:
        with open(arquivo, 'r') as file:
            for linha in file:
                nome = linha.split()[0]
                data = linha.split()[1]
                dia = int(data[:2])
                mes = int(data[2:4])
                ano = int(data[4:])
                idade = ano_atual - ano
                if mes_atual <= mes:
                    if mes_atual < mes:
                        idade -= 1
                    elif dia_atual < dia:
                        idade -= 1
                idade = str(idade)
                saida.write(nome + ' ')
                saida.write(idade + '\n')
