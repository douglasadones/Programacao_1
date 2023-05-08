'''Implemente um controle simples de mercadorias em uma despensa doméstica. Sobre cada
produto podem ser armazenado um código numérico, descrição e quantidade atual. O
programa deve ter opções para entrada e retirada de produtos, bem como um relatório geral
de produtos e suas quantidades em estoque. Seu programa também deve gerar um relatório
com os produtos não disponíveis (que estão com estoque vazio). Armazene os dados em
arquivo.'''

opcoes = '''Controle de Estoque
1 - Para entrada de produto
2 - Para saída de produto
3 - Relatório Geral
4 - Produtos indisponíveis
5 - sair'''


def menu():
    print(opcoes)
    op = int(input('Sua escolha: '))
    return op


op = menu()

while op != 5:
    op = menu()
    if op == 1:
        nome_produto = input('Informe o nome do produto: ')
        quant_entrada = int(input('Informe a quantidade: '))
        produtos = []
        with open('arquivo.txt', 'r') as file:
            index = 0
            for c in file:
                formatado = c.split()
                produtos.extend([formatado])
            print(produtos)
            for i in produtos:
                if nome_produto in i:
                    soma = str(int(i[2]) + quant_entrada)
                    i.pop(2)
                    i.insert(2, soma)
        with open('arquivo.txt', 'w') as file:
            for c in produtos:
                file.write(c[0] + ' ' + c[1] + ' ' + c[2] + '\n')
    elif op == 2:
        nome_produto = input('Informe o nome do produto: ')
        quant_saida = int(input('Informe a quantidade: '))
        produtos = []
        with open('arquivo.txt', 'r') as file:
            index = 0
            for c in file:
                formatado = c.split()
                produtos.extend([formatado])
            for i in produtos:
                if nome_produto in i:
                    subtracao = int(i[2]) - quant_saida
                    if subtracao < 0:
                        subtracao = 0
                    subtracao = str(subtracao)
                    i.pop(2)
                    i.insert(2, subtracao)
        with open('arquivo.txt', 'w') as file:
            for c in produtos:
                file.write(c[0] + ' ' + c[1] + ' ' + c[2] + '\n')
    elif op == 3:
        print('\nRelatório Geral')
        with open('arquivo.txt', 'r') as file:
            for linha in file:
                formatado = linha.split()
                print(f'Cod do Produto: {formatado[0]}\nDescrição: {formatado[1]}\nQuantidade atual: {formatado[2]}\n')
    elif op == 4:
        print('\nProdutos indisponíveis:')
        with open('arquivo.txt', 'r') as file:
            for linha in file:
                formatado = linha.split()
                if formatado[2] == '0':
                    print(f'Código: {formatado[0]}\nDescrição: {formatado[1]}\nQuantidade atual: {formatado[2]}\n')
    else:
        pass