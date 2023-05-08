"""Faça um programa que permita que o usuário entre com diversos nomes e telefone para
cadastro, e crie um arquivo com essas informações, com cada par de dados (nome e telefone)
em cada linha. O usuário finaliza a entrada com string vazia para nome e 0 para o telefone."""

with open('arquivo.txt', 'w') as file:
    while True:
        cadastro_atual = []
        nome = input('Informe o nome: ')
        if nome == '':
            break
        fone = input('Informe o telefone: ')
        if fone == '0':
            break
        cadastro_atual.extend([nome, fone])
        for c in cadastro_atual:
            file.write(c + ' ')
        file.write('\n')
