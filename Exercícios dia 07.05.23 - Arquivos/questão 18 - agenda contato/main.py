'''
Faça um programa que gerencia uma agenda de contatos. Para cada contato armazene o
nome da pessoa, o telefone e o aniversário (DD/MM/AAAA). O programa deve permitir (1)
inserir contato, (2) remover contato, (3) pesquisar um contato pelo nome, (4) listar todos os
contatos, (5) listar os contatos cujo nome inicia com uma dada letra, (6) imprimir os
aniversariantes do mês. Sempre que o programa for encerrado, os contatos devem ser
armazenados em um arquivo. Quando o programa iniciar, os contatos armazenados no
arquivo devem ser transferidos para alguma estrutura para manipulação.
'''
import datetime
from datetime import date


def menu():
    print(opcoes)
    op = int(input('Sua escolha: '))
    return op


def verificando_vazio():
    vazio = True
    with open('contatos.txt', 'r') as file:
        for c in file:
            lista = c.split()
            if len(lista) != 0:
                vazio = False
    return vazio


opcoes = '''1 - Para inserir contato
2 - Para remover contato
3 - Para pesquisar um contato pelo nome
4 - Para listar todos os contatos
5 - Para listar os contatos que iniciam com determinada letra
6 - Para listar os aniversariantes do mês'''

try:
    file = open('contatos.txt', 'r')
    file.close()
except:
    file = open('contatos.txt', 'w')
    file.close()

while True:
    op = menu()
    if op == 1:
        nome = input('Informe o nome da pessoa: ').lower()
        fone = input('Informe o número: ')
        data = input('Informe a data de aniversário(DDMMAAAA): ')
        with open('contatos.txt', 'a') as file:
            file.write(nome + ' ' + fone + ' ' + data + '\n')
    elif op == 2:
        if not verificando_vazio():
            pass
        else:
            print('Agenda atualmente vazia!')
    elif op == 3:
        nome_contato = input('Informe o nome: ')
        with open('contatos.txt', 'r') as file:
            for c in file:
                formatado = c.split()
                if nome_contato in formatado:
                    print('\nINFORMAÇÕES DO CONTATO:')
                    dia_aniv = formatado[2][:2]
                    mes_aniv = formatado[2][2:4]
                    ano_aniv = formatado[2][4:]
                    print(f'Número: {formatado[1]}\nAniversário: '
                          f'{dia_aniv}/{mes_aniv}/{ano_aniv}\n')
    elif op == 4:
        with open('contatos.txt', 'r') as file:
            print('\nTODOS OS CONTATOS:')
            for c in file:
                formatado = c.split()
                dia_aniv = formatado[2][:2]
                mes_aniv = formatado[2][2:4]
                ano_aniv = formatado[2][4:]
                print(f'Nome: {formatado[0]}\nNúmero: {formatado[1]}\nAniversário: '
                      f'{dia_aniv}/{mes_aniv}/{ano_aniv}\n')
    elif op == 5:
        letra = input('Informe a letra: ').lower()
        with open('contatos.txt', 'r') as file:
            print(f'\nContatos com a letra {letra.upper()}:')
            for c in file:
                if c[0][0] == letra:
                    formatado = c.split()
                    dia_aniv = formatado[2][:2]
                    mes_aniv = formatado[2][2:4]
                    ano_aniv = formatado[2][4:]
                    print(f'Nome: {formatado[0]}\nNúmero: {formatado[1]}\nAniversário: '
                          f'{dia_aniv}/{mes_aniv}/{ano_aniv}\n')
    elif op == 6:
        mes_atual = date.today().month
        with open('contatos.txt', 'r') as file:
            print('\nTODOS OS ANIVERSARIANTES DO MÊS:')
            for c in file:
                formatado = c.split()
                dia_aniv = formatado[2][:2]
                mes_aniv = formatado[2][2:4]
                ano_aniv = formatado[2][4:]
                if int(mes_aniv) == mes_atual:
                    print(f'Nome: {formatado[0]}\nNúmero: {formatado[1]}\nAniversário: '
                          f'{dia_aniv}/{mes_aniv}/{ano_aniv}\n')
