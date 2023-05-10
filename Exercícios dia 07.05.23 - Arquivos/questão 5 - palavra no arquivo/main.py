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
        for linha in file:  # String completa da linha
            ocorrencia = ''
            for caractere in linha:  # caractere por caractere da linha
                if caractere.isalpha():
                    ocorrencia += caractere.lower()
                else:
                    if palavra == ocorrencia:
                        contador += 1
                        ocorrencia = ''
                    else:
                        ocorrencia = ''
    print(contador)
