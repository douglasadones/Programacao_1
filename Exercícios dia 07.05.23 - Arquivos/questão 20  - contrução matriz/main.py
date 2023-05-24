# dados = []
# with open('matriz.txt', 'r') as file:
#     for c in file:  # Obtendo informações para manipulação
#         dado = c.strip().split()
#         for c in range(len(dado)):  # Transformando os dados em inteiros
#             dado[c] = int(dado[c])
#         dados.append(dado)
# linhas = dados[0][0]
# colunas = dados[0][1]
# quant_anulados = dados[0][2]  # não encontrei utilidade para esse dado
# pos_anulados = dados[1:]
#
# matriz = []
# for n in range(linhas):
#     temp = []
#     for m in range(colunas):
#         if [n, m] in pos_anulados:
#             temp.append(0)
#         else:
#             temp.append(1)
#     matriz.extend([temp])
#
# for c in matriz:
#     print(*c)
#
#
# # Resposta do professor ---------------------
#
#

# matriz 3 por 3
def mostrar(matriz):
    for i in matriz:
        print(*i, sep=" ")


def montar_matriz_dic(n, m):
    matriz = {}
    for i in range(n):
        for j in range(m):
            matriz[(i, j)] = 1
    return matriz


def montar_matriz_lista(n, m):
    matriz = []
    for i in range(n):
        linha = [1] * m
        matriz.append(linha)
    return matriz


lista = [[1, 1, 1], [1, 1, 1], [1, 1, 1]]


dicionario = {(0, 0): 1, (0, 1): 1, (0, 2): 1, (1, 0): 1, (1, 1): 1, (1, 2): 1, (2, 0): 1, (2, 1): 1, (2, 2): 1}


with open('matriz.txt', 'r') as file:
    n, m, q = 0, 0, 0
    for linha in file:
        linha = linha.strip().split()
        if len(linha) > 2:
            n = int(linha[0])
            m = int(linha[1])
            q = int(linha[2])
            matriz = montar_matriz_lista(n, m)
            # dic = montar_matriz_dic(n, m)
        else:
            i = int(linha[0])
            j = int(linha[1])
            matriz[i][j] = 0  # Se for na lista
            # dic[(i, j)] = 0  # Se for no dicionário
    mostrar(matriz)
