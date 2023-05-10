'''Desenvolver um programa que lê o conteúdo de um arquivo e cria um arquivo com o mesmo
conteúdo, mas com todas as letras minúsculas convertidas para maiúsculas. Os nomes dos
arquivos serão fornecidos, via teclado, pelo usuário. (Use a função da linguagem que converte
maiúscula para minúscula). Aplique-a a cada caractere da string.'''

arquivo = input('Informe o nome do arquivo: ')

existe = False

try:
    file = open(arquivo, 'r')
    file.close()
    existe = True
except:
    print('Arquivo não encontrado!')


if existe:
    with open('maiusculo.txt', 'w') as file1:
        with open(arquivo, 'r') as file2:
            for linhas in file2:
                for caractere in linhas:
                    if caractere.isupper():
                        file1.write(caractere)
                    else:
                        file1.write(caractere.upper())
