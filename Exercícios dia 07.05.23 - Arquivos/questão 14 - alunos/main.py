'''Crie um programa que receba como entrada o número de alunos de uma disciplina. Crie
estrutura(s) para armazenar as informações a respeito desses alunos. Após a leitura,
armazene os dados (nome do aluno e sua nota final) em um arquivo. Cada linha do arquivo
contém dados de um aluno. Use nomes com no máximo 40 caracteres. Se o nome não
contém 40 caracteres, complete com espaços em branco.'''

quant = int(input('Informe a quantidade de alunos na disciplina: '))
with open('arquivo.txt', 'w') as file:
    for aluno in range(1, quant + 1):
        nome = input(f'Nome do {aluno}º aluno: ').capitalize()
        if len(nome) > 40:
            print('Nome inválido!')
            break
        nota = input(f'Nota final do aluno: ')
        file.write(f'{nome:<40}' + ' ' + nota + '\n')
