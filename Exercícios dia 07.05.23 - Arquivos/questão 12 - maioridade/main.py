'''Faça um programa que recebe como entrada o nome de um arquivo de entrada e o nome de
um arquivo de saída e o ano corrente. Cada linha do arquivo de entrada contém o nome de
uma pessoa e o seu ano de nascimento. A rotina deverá ler o arquivo de entrada e gerar um
arquivo de saída onde aparece o nome da pessoa e sua idade. Se a idade for menor do que
18 anos, escrever menor de idade. Se a idade for maior do que 18 anos, escrever maior de
idade. Se a idade for igual a 18 anos, escrever entrando na maior idade.'''

men_idade = 'Menor de Idade'
mai_idade = 'Maior de Idade'
ent_maio = 'Entrando na Maior Idade'

existe = False
arq_ent = input('Informe o nome do arquivo de entrada: ')
arq_sai = input('Informe o nome do arquivo de saída: ')
ano_corrente = int(input('Informe o ano corrente: '))

try:
    file = open(arq_ent, 'r')
    file.close()
    existe = True
except:
    print('Arquivo não encontrado!')

if existe:
    lista_geral = []
    with open(arq_sai, 'w') as saida:
        with open(arq_ent, 'r') as entrada:
            for linha in entrada:
                formatado = linha.split()
                idade = ano_corrente - int(formatado[1])
                if idade < 18:
                    status_da_idade = men_idade
                elif idade == 18:
                    status_da_idade = ent_maio
                else:
                    status_da_idade = mai_idade
                lista_geral.extend([[formatado[0], idade, status_da_idade]])
            print(lista_geral)
        for pessoa in lista_geral:
            saida.write(pessoa[0] + ' ' + str(pessoa[1]) + ' ' + pessoa[2] + '\n')

