class Car():
    def __init__(self, cor, portas, rodas):
        self.__cor = cor
        self.__portas = portas
        self.__rodas = rodas

    def get_cor(self):
        print(self.__cor)

    def set_cor(self, cor):
        self.__cor = cor



