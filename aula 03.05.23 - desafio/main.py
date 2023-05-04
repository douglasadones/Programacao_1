def criando_lista():
    lista_geral = []
    with open('arquivo.txt', 'r') as file:
        for num, l in enumerate(file):
            tratado = ''.join(l).split()
            lista_geral.append(tratado)
        return lista_geral


def criando_dict(arquivo_tratado):
    dic_geral = {}
    for c in range(1, int(arquivo_tratado[0][0]) + 1):  # aqui o 'c' representa a key atual do dicionário
        lista = criando_lista()  # backup para poder usar o remove em cada loop e ainda sim ter acesso a lista completa
        combinacoes = []  # lista momentânea que armazena todas as combinações encontradas
        for i in lista[1:]:
            if str(c) in i:  # Condição: Se a key estiver na lista do momento
                i.remove(str(c))
                combinacoes.append(i[0])
        dic_geral[c] = combinacoes  # Criação da key + value
    return dic_geral


def principal():
    lista = criando_lista()
    dicionario = criando_dict(lista)
    for k, v in dicionario.items():
        print(f'{k}:', end=' ')
        print(*v, sep=',')


if __name__ == '__main__':
    principal()
