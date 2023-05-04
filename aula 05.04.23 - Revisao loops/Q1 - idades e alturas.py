"""Crie um programa que lê as idades e alturas de alguns alunos. A condição de parada é
altura = 0. Em seguida, o programa deve informar quantos alunos com mais de 13 anos possuem
altura inferior à 1.5 m."""

alunos_cadastrados = []
alunos_que_satisfazem_as_condicoes = 0

while True:
    altura = float(input("Informe a altura: "))
    if altura == 0:
        break
    idade = int(input("Informe a idade: "))
    print("Cadastrado!")
    alunos_cadastrados.extend([[idade, altura]])

for alunos in alunos_cadastrados:
    if alunos[0] > 13 and alunos[1] < 1.5:
        alunos_que_satisfazem_as_condicoes += 1

print(f"Total de lunos com mais de 13 anos com altura inferior à 1.5m: {alunos_que_satisfazem_as_condicoes} ")

