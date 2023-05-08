'''Codifique, compile e execute um programa que leia a profissão e o questão 13 - tempo de serviço (em
anos), de cada um dos 50 funcionários de uma empresa e armazene-os no arquivo
”empresa.txt”. Cada linha do arquivo corresponde aos dados de um funcionários. Em seguida,
leia o mesmo arquivo utilizando e apresente os dados na tela.'''

dados = []
while True:
    profissao = input('Informe a profissão: ').capitalize()
    if profissao == '':
        break
    tempo = input('Informe o tempo (anos): ')
    if tempo == '0':
        break
    dados.extend([[profissao, tempo]])
    print(dados)

with open('empresa.txt', 'w') as file:
    for c in dados:
        print(c)
        file.write(c[0] + ' ' + c[1] + '\n')

with open('empresa.txt', 'r') as file:
    for num, c in enumerate(file):
        formatado = c.split()
        print(f'Funcionário {num + 1}:\nProfissão: {formatado[0]}\nTempo de serviço: {formatado[1]} anos.\n')
