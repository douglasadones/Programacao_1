"""Codifique um programa, que manipule um arquivo contendo resgistros descritos pelos seguintes campos: código do
vendedor, nome do vendedor, valor da venda e mês de referência. A manipulação do arquivo em questão é feita através
da execução das operações disponibilizadas pelo menu. Obs: Os registros devem estar ordenados no arquivo, de forma
crescente, de acordo com as informações contidas nos campos código do vendedor e mês. Não deve existir mais de um
registro no arquivo com os mesmos valores nos campos código do vendedor e mês."""


def mostrar():
    print("\n======== REGISTROS =======")
    with open('arquivo.txt', 'r') as file:
        for c in file:
            formatado = c.strip().split()
            print(f'Código: {formatado[0]}\nVendedor: {formatado[1]}'
                  f'\nValor: R$ {formatado[2]}\nMês: {formatado[3]:0>2}')
            print('=' * 25)
    print()


def arq_em_lista():
    """Preenche e retorna uma lista com todos os dados atuais do arquivo"""
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
    """Verifica se existe o nome do vendedor na lista. Em caso afirmativo, retorna seu index positivo. Em caso negativo,
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


def add_registro(codigo, nome, valor, mes):
    with open('arquivo.txt', 'a') as file:
        file.write(codigo + ' ' + nome + ' ' + valor + ' ' + mes + '\n')
    ordenar_arq()


def alt_valor(nome, valor):
    lista = arq_em_lista()
    index = index_vendedor(nome)
    if index != -1:
        lista[index][2] = str(valor)
        del_registro(nome)
        add_registro(lista[index][0], lista[index][1], lista[index][2], lista[index][3])
        return True
    else:
        return False


def menu():
    print(string_menu)
    op = int(input("Sua escolha: "))
    return op


def excluir_arquivo():
    file = open('arquivo.txt', 'w')
    file.close()
    print('Arquivo Apagado!')


def ordenar_arq():
    """Ordena o arquivo de forma crescente usando o código do vendedor como referência"""
    lista = arq_em_lista()
    for c in lista:  # Transformando os códigos de vendedores em inteiros para posterior manipulação
        c[0] = int(c[0])

    for c in range(len(lista) - 1, 0, -1):  # Usando o método da bolha para ordenar de forma crescente
        for i in range(c):
            if lista[i] > lista[i+1]:
                lista[i], lista[i+1] = lista[i+1], lista[i]

    with open('arquivo.txt', 'w') as file:
        for c in lista:
            file.write(str(c[0]) + ' ' + c[1] + ' ' + c[2] + ' ' + c[3] + '\n')


string_menu = """1 - Para criar o arquivo de dados;
2 - Para incluir um determinado registro no arquivo;
3 - Para excluir um determinado vendedor no arquivo;
4 - Para alterar o valor de uma venda no arquivo;
5 - Para imprimir os registros na saída padrão;
6 - Para excluir o arquivo de dados;
7 - Para finalizar o programa."""

while True:
    op = menu()
    if op == 1:  # criar aquivo
        if not arq_existe():
            with open('arquivo.txt', 'w') as file:
                print('\nARQUIVO CRIADO\n')
        else:
            print('\nO arquivo já foi criado!\n')
    elif op == 2:  # Adicionar
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
        if arq_existe():
            add_registro(codigo, nome, valor, mes)
        else:
            print('\nArquivo Inexistente\n')
    elif op == 3:  # Excluir
        nome = input('Informe o nome do vendedor: ')
        if arq_existe():
            del_registro(nome)
    elif op == 4:  # Alterar
        nome = input('Informe o nome do vendedor: ')
        if index_vendedor(nome) == -1:
            print('\nCADASTRO NÃO ENCONTRADO\n')
        else:
            valor = int(input("Informe o valor atualizado: "))
            alt_valor(nome, valor)
            print('\nVALOR DA VENDA ATUALIZADO!\n')
    elif op == 5:  # Imprimir Registro
        mostrar()
    elif op == 6:  # Excluir o arquivo de dados
        seg = input(input('Esta ação irá apagar todos os registros. apagar?(0 para não, 1 para sim): '))
        if seg == 1:
            excluir_arquivo()
        else:
            continue
    elif op == 7:
        break
    else:
        continue
