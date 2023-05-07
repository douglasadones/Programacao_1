'''Faça um programa que receba dois arquivos do usuário, e crie um terceiro arquivo com o
conteúdo dos dois primeiros juntos (o conteúdo do primeiro seguido do conteúdo do segundo).'''


existem = existe_1 = existe_2 = False
arq_inexistentes = []

# ---------------- Garantindo o que a entrada não seja vazia ----------------
arq_1 = input('Informe o nome do 1º arquivo: ')
while arq_1 == '':
    arq_1 = input('Informe o nome do 1º arquivo: ')

arq_2 = input('Informe o nome do 2º arquivo: ')
while arq_2 == '':
    arq_2 = input('Informe o nome do 2º arquivo: ')

# ---------------- Verificando se ambos os arquivos existem ----------------
try:
    file1 = open(arq_1, 'r')
    file1.close()
    existe_1 = True
except:
    arq_inexistentes.append(arq_1)
try:
    file2 = open(arq_2, 'r')
    while file2 == '':
        file2 = open(arq_2, 'r')
    file2.close()
    existe_2 = True
except:
    arq_inexistentes.append(arq_2)
if existe_1 == existe_2 and existe_1:
    existem = True

# --------------------------- Juntando informações ---------------------------
if existem:
    with open('arquivo_junção.txt', 'w') as terceiro_arquivo:
        with open(arq_1, 'r') as file:
            for linha in file:
                terceiro_arquivo.write(linha)
            terceiro_arquivo.write('\n')
        with open(arq_2, 'r') as file:
            for linha in file:
                terceiro_arquivo.write(linha)
else:
    print('Erro! Arquivo(s) não encontrado(s): ')
    for item in arq_inexistentes:
        print(item)


