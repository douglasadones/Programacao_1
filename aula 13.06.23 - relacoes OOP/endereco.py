class Endereco:
    def __init__(self, rua, numero, cidade):
        self.rua = rua
        self.numero = numero
        self.cidade = cidade

    def __del__(self):  # Apagando o objeto Ana, podemos ver a composição funcionando aqui!
        print(f"Apagando objeto {self.rua}")
