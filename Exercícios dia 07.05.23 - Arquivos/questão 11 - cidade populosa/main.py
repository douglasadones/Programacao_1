'''Faça um programa que recebe como entrada o nome de um arquivo de entrada e o nome de
um arquivo de saída. O arquivo de entrada contém em cada linha o nome de uma cidade e o
seu número de habitantes. A rotina deverá ler o arquivo de entrada e gerar um arquivo de
saída onde aparece o nome da cidade mais populosa seguida pelo seu número de habitantes.'''

existe = False
arq_ent = input('Informe o nome do arquivo de entrada: ')
arq_sai = input('Informe o nome do arquivo de saída: ')

try:
    file = open(arq_ent, 'r')
    file.close()
    existe = True
except:
    print('Arquivo não encontrado!')

# ------------------- Verificando a cidade mais populosa -------------------
if existe:
    with open(arq_sai, 'w') as saida:
        with open(arq_ent, 'r') as entrada:
            mais_populosa = []
            for num, linha in enumerate(entrada):
                separado = linha.split()
                habitantes = int(separado[-1])
                if len(separado) > 2:  # Separando o nome da cidade do num de habitante
                    nome_cidade = len(separado) - 1
                else:
                    nome_cidade = 1
                if num == 0:
                    mais_populosa.extend([separado[:nome_cidade], separado[-1]])
                elif habitantes > int(mais_populosa[-1]):
                    mais_populosa = []
                    mais_populosa.extend([separado[:nome_cidade], separado[-1]])
            for c in mais_populosa[0]:
                saida.write(c + ' ')
            saida.write(mais_populosa[-1])
