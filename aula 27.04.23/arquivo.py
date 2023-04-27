def criar(arquivo):
    file = open(arquivo, "w")
    return file


def abrir(arquivo):
    file = open(arquivo, "r")
    return file


def anexar(arquivo):
    file = open(arquivo, "a")
    return file


def cadastrar(file):
    while True:
        valor = input("Valor(es): ")
        if valor == "":
            break
        file.write(valor+"\n")


def mostrar(file):
    for valor in file:
        print(valor)


def principal():
    arquivo = input("Nome do arquivo: ")
    file = criar(arquivo)
    cadastrar(file)
    file.close()
    file = abrir(arquivo)
    mostrar(file)
    file.close()
    file = anexar(arquivo)
    cadastrar(file)
    file.close()
    file = abrir(arquivo)
    mostrar(file)
    file.close()


if __name__ == "__main__":
    principal()