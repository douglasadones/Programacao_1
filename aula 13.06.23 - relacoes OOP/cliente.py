from endereco import Endereco


class Cliente:
    def __init__(self, nome):
        self.nome = nome
        self.enderecos = []

    def inserir_endereco(self, rua, numero, cidade):
        self.enderecos.append(Endereco(rua, numero, cidade))

    def mostrar_endereco(self):
        for e in self.enderecos:
            print(e.rua, e.numero, e.cidade)

    def __del__(self):
        print(f"Apagando o objeto {self.nome}")


if __name__ == "__main__":
    while True:
        print("Tecle apenas ENTER para terminar")
        nome = input("Nome: ")
        if nome == "" or nome == []:
            break
        c1 = Cliente(nome)  # nome
        while True:
            print("Tecle apenas ENTER para terminar a leitura de endereços")
            endereco = input("Endereço: ").split()
            if endereco == "" or endereco == []:
                break
            c1.inserir_endereco(endereco[0], endereco[1], endereco[2])

    c1.mostrar_endereco()
    del c1