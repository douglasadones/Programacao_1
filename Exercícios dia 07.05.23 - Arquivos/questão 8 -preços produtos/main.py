'''Faça um programa que leia um arquivo com os preços de diversos produtos, e calcule o total
da compra.'''

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
    with open(arquivo, 'r') as file:
        for linha in file:
            formatado = (linha.split())
            contador += float(formatado[1])
    print(f'O total da compra é: R$ {contador:.2f}')
