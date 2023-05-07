def menu():
    title = ' CADASTRO '
    print(f'{title:*^40}')
    print('1. Cadastrar Usuários\n2. Mostrar Cadastros\n3. Pesquisar um Cadastro\n4. Deletar um cadastro\n5. Sair')
    escolha = int(input('Sua escolha: '))
    print()
    return escolha


def cadastrar():
    nome = input('Nome: ').capitalize().strip()
    if nome == "":
        return nome
    fone = input('Fone: ')
    while len(fone) != 11:
        print('Número inválido! Por favor, digite novamente')
        fone = input('Fone: ')
    nascimento = input('Nascimento (DDMMAAAA): ')
    while len(nascimento) != 8 or int(nascimento[:2]) > 31 or int(nascimento[2:4]) > 12:
        print('Data inválida! Por favor, digite novamente')
        nascimento = input('Nascimento (DDMMAAAA): ')
    with open('cadastro.txt', 'a') as file:
        file.write(f'{nome} {fone} {nascimento}' + '\n')
        file.close()


def mostrar():
    with open('cadastro.txt', 'r') as file:
        print()
        for info in file:
            lista = info.split()
            print(f'Nome: {lista[0]}\nFone: ({lista[1][0:2]}) {lista[1][2]}-{lista[1][3:7]}-{lista[1][7:]}'
                  f'\nNascimento: {lista[2][0:2]}/{lista[2][2:4]}/{lista[2][4:]}')
            print('=' * 25)
        print()


def mostrar_cadastro_unico(cadastro):
    with open('cadastro.txt', 'r') as file:
        if pesquisar(cadastro):
            for c in file:
                lista = c.split()
                if lista[0] == cadastro:
                    print()
                    print(f'Nome: {lista[0]}\nFone: ({lista[1][0:2]}) {lista[1][2]}-{lista[1][3:7]}-{lista[1][7:]}'
                          f'\nNascimento: {lista[2][0:2]}/{lista[2][2:4]}/{lista[2][4:]}')
        else:
            print('Cadastro Inexistente')


def pesquisar(nome):
    with open('cadastro.txt', 'r') as file:
        for cadastro in file:
            lista = cadastro.split()
            if lista[0] == nome:
                return True
        return False


def deletar(nome):
    if pesquisar(nome):
        with open('cadastro.txt', 'r') as file:
            lista_cadastros = []
            for c in file:  # Preenchendo a lista com todos os cadastros
                lista_cadastros.append(c.split())

            for i in lista_cadastros:  # Deletando cadastro informado
                if i[0] == nome:
                    lista_cadastros.pop(lista_cadastros.index(i))

        with open('cadastro.txt', 'w') as file:  # Reescrevendo o arquivo
            for c in lista_cadastros:
                tratado = ' '.join(c)
                file.write(tratado + '\n')
    else:
        print('Cadastro Inexistente')


try:
    file = open('cadastro.txt', 'r')
    file.close()
except:
    file = open('cadastro.txt', 'w')
    file.close()

while True:
    op = menu()
    if op == 1:  # Cadastrar
        print('Para terminar, pressione enter no campo "Nome"')
        while True:
            op = cadastrar()
            if op == "":
                break
        mostrar()
    elif op == 2:  # Mostrar
        mostrar()
    elif op == 3:  # Pesquisar
        nome = input('Informe o nome: ').capitalize().strip()
        mostrar_cadastro_unico(nome)
    elif op == 4:  # Deletar
        nome = input('Informe o nome: ').capitalize().strip()
        deletar(nome)
    elif op == 5:  # Sair
        break
    else:
        print('Escolha inválida!')
        continue
    print()
