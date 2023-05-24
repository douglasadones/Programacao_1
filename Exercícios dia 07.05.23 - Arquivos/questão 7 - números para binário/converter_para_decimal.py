with open('convertido.txt', 'r') as file:
    list = []
    for c in file:
        reformatando = c.split()[0][::-1]  # invertendo por conta das potencias
        list.append(reformatando)

print(list)

lista_convertida = []
for index, c in enumerate(list):
    somatorio = 0
    for i in c:
        if i == '1':
            somatorio += pow(2, index)
    lista_convertida.append(somatorio)

print(lista_convertida)
