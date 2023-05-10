dados = []
with open('matriz.txt', 'r') as file:
    for c in file:  # Obtendo informações para manipulação
        dado = c.strip().split()
        for c in range(len(dado)):  # Transformando os dados em inteiros
            dado[c] = int(dado[c])
        dados.append(dado)
linhas = dados[0][0]
colunas = dados[0][1]
quant_anulados = dados[0][2]  # não encontrei utilidade para esse dado
pos_anulados = dados[1:]


matriz = []
for n in range(linhas):
    temp = []
    for m in range(colunas):
        if [n, m] in pos_anulados:
            temp.append(0)
        else:
            temp.append(1)
    matriz.extend([temp])

for c in matriz:
    print(*c)
