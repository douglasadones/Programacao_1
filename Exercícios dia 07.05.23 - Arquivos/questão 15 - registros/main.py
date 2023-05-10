"""Codifique um programa, que manipule um arquivo contendo resgistros descritos pelos seguintes campos: código do
vendedor, nome do vendedor, valor da venda e mês de referência. A manipulação do arquivo em questão é feita através
da execução das operações disponibilizadas pelo menu. Obs: Os registros devem estar ordenados no arquivo, de forma
crescente, de acordo com as informações contidas nos campos código do vendedor e mês. Não deve existir mais de um
registro no arquivo com os mesmos valores nos campos código ddo vendedor e mês."""


def ordenar_arq():
    pass


def arq_em_lista():
    lista_geral = []
    with open('arquivo.txt', 'r') as file:
        for c in file:
            separado = c.split()
            lista_geral.extend([separado])
    return lista_geral


def arq_existe():
    try:
        file = open('arquivo.txt', 'r')
        file.close()
        return True
    except:
        return False


def index_vendedor(nome):
    """Verifica se existe o nome do vendedor na lista. Em caso afirmativo,r etorna seu index. Em caso denativo
     retorna -1"""
    registros = arq_em_lista()
    for c in registros:
        if nome in c:
            return registros.index(c)
    return -1


def del_registro(nome):
    registros = arq_em_lista()
    index = index_vendedor(nome)
    if index == -1:
        print('\nVendedor não cadastrado!\n')
    else:
        registros.pop(index)
        with open('arquivo.txt', 'w') as file:
            for c in registros:
                file.write(c[0] + ' ' + c[1] + ' ' + c[2] + ' ' + c[3] + '\n')
        print('\nVENDEDOR EXCLUÍDO\n')


def add_registro():
    with open('arquivo.txt', 'a') as file:
        cadastros = arq_em_lista()
        codigo = input('Informe o código do vendedor: ')
        while codigo in cadastros:
            print('Código já cadastrado!')
            codigo = input('Informe o código do vendedor: ')
        nome = input('Informe o nome do vendedor: ')
        valor = input('Informe o valor da venda: ')
        mes = input('Informe o mês: ')
        while mes in cadastros:
            print('Mês já cadastrado!')
            mes = input('Informe o mês: ')
        file.write(codigo + ' ' + nome + ' ' + valor + ' ' + mes + '\n')


def alt_valor(nome, valor=None):
    lista = arq_em_lista()
    index = index_vendedor(nome)
    if index != -1:
        lista[index][2] = valor
        # Tô aqui _---------------------------------------------------------------------------------
        return True
    else:
        return False


def menu():
    print(string_menu)
    op = int(input("Sua escolha: "))
    return op


string_menu = """1 - Para criar o arquivo de dados;
2 - Para incluir um determinado registro no arquivo;
3 - Para excluir um determinado vendedor no arquivo;
4 - Para alterar o valor de uma venda no arquivo;
5 - Para imprimir os registros na saída padrão;
6 - Para excluir o arquivo de dados;
7 - Para finalizar o programa.
"""

while True:
    op = menu()
    if op == 1:
        if not arq_existe():
            with open('arquivo.txt', 'w') as file:
                print('\nARQUIVO CRIADO\n')
        else:
            print('\nO arquivo já foi criado\n!')
    elif op == 2:
        if arq_existe():
            add_registro()
        else:
            print('\nArquivo Inexistente\n')
    elif op == 3:
        nome = input('Informe o nome do vendedor: ')
        if arq_existe():
            del_registro(nome)
    elif op == 4:
        nome = input('Informe o nome do vendedor: ')
        if not alt_valor(nome):
            print('\nCADASTRO NÃO ENCONTRADO\n')
        else:
            valor = int(input("Informe o valor atualizado: "))
            alt_valor(nome, valor)
            print('\nVALOR DA VENDA ATUALIZADO!\n')