'''Faça um programa que receba do usuário um arquivo, e mostre na tela quantas linhas tem
esse arquivo. Teste o programa com arquivos de quantidade de linhas variáveis.'''

arquivo = input('Informe o nome do arquivo: ')

existe = False

try:
    file = open(arquivo, 'r')
    file.close()
    existe = True
except:
    print('Arquivo não encontrado!')


if existe:
    with open(arquivo, 'r') as file:
        com_info = sem_info = 0
        for linhas in file:
            if len(linhas) - 1 != 0:
                com_info += 1
            else:
                sem_info += 1
        print(f'Seu arquivo possui {com_info} linha(s) com informações e {sem_info + 1} linha(s) sem informações.')
