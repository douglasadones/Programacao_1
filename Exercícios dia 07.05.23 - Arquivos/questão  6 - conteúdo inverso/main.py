'''Faça um programa que recebe como entrada o nome de um arquivo de entrada e o nome de
um arquivo de saída. Cada linha do arquivo de entrada possui colunas de tamanho de 30
caracteres. No arquivo de saída deverá ser escrito o arquivo de entrada de forma inversa.'''

arquivo = input('Informe o nome do arquivo: ')
existe = False

try:
    file = open(arquivo, 'r')
    file.close()
    existe = True
except:
    print('Arquivo não encontrado!')


if existe:
    contador = 0
    reorganizado = []

    with open('arquivo_inverso.txt', 'w') as inverso:
        with open(arquivo, 'r') as file:
            for linha in file:
                palavra = linha[::-1]
                reorganizado.insert(0, palavra)
        for itens in reorganizado:
            inverso.write(itens)

