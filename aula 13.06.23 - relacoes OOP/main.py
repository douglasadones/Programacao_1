from produto import Produto
from nota_fiscal_Usando_agregação import NotaFiscal

produtos = list()


def buscar_produto(codigo):
    for produto in produtos:
        if produto.codigo == codigo:
            return produto
    return None


if __name__ == '__main__':
    with open('dados.txt', 'r') as file:
        linhas = [linha.strip().split() for linha in file]
    for linha in linhas:
        produtos.append(Produto(int(linha[0]), linha[1], float(linha[2])))

    nf = NotaFiscal()
    while True:
        print('Para concluir a venda, informe código 0 (zero)')
        codigo = int(input('Código do produto: '))
        if codigo == 0:
            break
        produto = buscar_produto(codigo)
        if produto:
            nf.inserir_produto(produto)
    nf.emitir_cupom()

