"""Em uma eleição para coordenação de curso com 15 eleitores existem 3 candidatos. Os
votos são informados por meio de código. Os códigos utilizados são: 1 – Candidato A; 2 – Candidato
B; 3 – Candidato C; 4 – Voto Nulo; e 5 – Voto Branco. Faça um programa que leia os votos de cada
eleitor, calcule e mostre: (1) O total de votos para cada candidato; (2) O total de votos nulos; (3) O
total de votos em branco; (4) A percentagem de votos nulos sobre o total de votos; e (5) A
percentagem de votos em branco sobre o total de votos."""

votos_cadastrados = {
    "Candidato A": 0,
    "Candidato B": 0,
    "Candidato C": 0,
    "Nulo": 0,
    "Branco": 0,
}

TOTAL_DE_VOTOS = 10

# ------------------------------------ Obtendo dados ----------------------------------------
for eleitores in range(TOTAL_DE_VOTOS):
    voto = int(input("Eleições para coordenação do curso\n1. Candidato A\n2. Candidato B\n3. Candidato C"
                     "\n4. Voto Nulo\n5. Voto Branco\nInforme seu voto: "))
    if voto == 1:
        votos_cadastrados['Candidato A'] += 1
    elif voto == 2:
        votos_cadastrados['Candidato B'] += 1
    elif voto == 3:
        votos_cadastrados['Candidato C'] += 1
    elif voto == 4:
        votos_cadastrados['Nulo'] += 1
    elif voto == 5:
        votos_cadastrados['Branco'] += 1
    else:
        print("Opção inválida")
        break

# ------------------------------------ Tratando e mostrando os dados ----------------------------------------

percentual_votos_nulos = round((votos_cadastrados["Nulo"] * 100 / TOTAL_DE_VOTOS), 2)
percentual_votos_brancos = round((votos_cadastrados["Branco"] * 100 / TOTAL_DE_VOTOS), 2)

print("Quantidade de votos de cada candidato:")
for key, value in votos_cadastrados.items():
    if key == "Nulo" or key == "Branco":
        continue
    print(f"{key}: {value} Voto(s)")

print(f"Total de votos nulos: {votos_cadastrados['Nulo']}")
print(f"Total de votos Brancos: {votos_cadastrados['Branco']}")
print(f"Percentual de votos nulos: {percentual_votos_nulos}")
print(f"Percentual de votos Brancos: {percentual_votos_brancos}")
