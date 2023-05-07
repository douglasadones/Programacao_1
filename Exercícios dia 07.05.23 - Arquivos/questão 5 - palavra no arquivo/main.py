'''Faça um programa no qual o usuário informa o nome do arquivo, e uma palavra, e retorne o
número de vezes que aquela palavra aparece no arquivo.'''

arquivo = input('Informe o nome do arquivo: ')
palavra = input('Informe uma palavra: ').lower()

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
            ocorrencia = ''
            for caractere in linha:
                if caractere != ' ':
                    ocorrencia += caractere.lower()
                if palavra in ocorrencia:
                    contador += 1
                    ocorrencia = ''
    print(contador)
