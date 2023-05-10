'''Abra um arquivo cujo nome é informado como argumento na linha de comando. Calcule e
escreva o número de caracteres, o número de linhas e o número de palavras neste arquivo.
Escreva também quantas vezes cada letra ocorre no arquivo (ignorando letras com acento).
Obs.: palavras são separadas por um ou mais caracteres espaço, tabulação ou nova linha.'''

quant_letras = {'a': 0, 'b': 0, 'c': 0, 'd': 0, 'e': 0, 'f': 0, 'g': 0, 'h': 0, 'i': 0, 'j': 0,
                'k': 0, 'l': 0, 'm': 0, 'n': 0, 'o': 0, 'p': 0, 'q': 0, 'r': 0, 's': 0, 't': 0,
                'u': 0, 'v': 0, 'w': 0, 'x': 0, 'y': 0, 'z': 0}

quant_caracteres = quant_palavras = quant_linhas = 0

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
        for linha in file:
            quant_linhas += 1
            separado = linha.split()
            quant_palavras += len(separado)
            for palavra in separado:
                for caractere in palavra:
                    quant_caracteres += 1
                    quant_letras[caractere.lower()] += 1

    print(f'Quantidade de linhas: {quant_linhas}\nQuantidade de Palavras: {quant_palavras}'
          f'\nQuantidade de caracteres: {quant_caracteres}')

    print('Ocorrencia das letras:')
    for k, v in quant_letras.items():
        if v != 0:
            print(f'Letra "{k}" apareceu {v} vez(es)')
