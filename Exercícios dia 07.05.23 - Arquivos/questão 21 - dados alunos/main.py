"""Faça um programa para gerenciar os dados e as notas dos alunos de uma turma com um menu contendo as
seguintes opções.
a) Faça a rotina que gerencia o menu, e para cada uma das opções deste menu, crie uma função específica.
b) O programa deve manipular dois arquivos ("aluno.txt" e "notas.txt"): O primeiro arquivo deverá armazenar,
para cada aluno, por linha: matrícula, nome e ano de nascimento. O segundo arquivo deverá armazenar por linha a
matrícula e três notas.
c) O programa deverá utilizar estruturas (tuplas, listas e/ou dicionario) para armazenar os dados dos alunos.
d) A cada leitura de dados, as mesmas devem ser gravadas nos respectivos arquivos."""

string_menu = """1 - Inserir aluno e notas;
2 - Inserir as notas dos alunos;
3 - Exibir alunos e notas;
4 - Exibir alunos e notas;
5 - Exibir alunos, notas e médias;
6 - Exibir alunos reprovados;
7 - Salvar dados em Disco;
0. Sair do programa (fim)."""

dic_geral = {}

try:
    with open('aluno.txt', 'r') as file:
        with open('notas.txt', 'r') as file2:
            cont = 0
            for c in file:
                print(c)
            for c in file2:
                print(c)
except:
    pass


def menu():
    print(string_menu)
    op = int(input("Sua escolha: "))
    return op


def add_aluno():
    pass


while True:
    op = menu()
    if op == 1:
        pass
    elif op == 0:
        break
    else:
        continue
