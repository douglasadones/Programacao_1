class Pessoa:
    sexo = "I"  # Todos os objetos terão este atributo e podem ser acessado com .sexo (Issó é um atributo estático)

    def __init__(self, nome: str, cpf: int):  # Só serve para tornar mais legível. Não força nenhum tipo específico.
        self.nome = nome
        self.__cpf = cpf

    def __get_cpf(self) -> int:  # Só serve para tornar mais legível o tipo de retorno. Não força nenhum tipo.
        return self.__cpf

    def mostrar(self):
        return self.__get_cpf()


print(Pessoa.sexo)  # Isso só funciona pq o atributo "sexo" está no contexto da classe.
print(Pessoa.nome)  # Isso n]ao funciona pq o atributo "sexo" está no contexto do objeto, logo, é exigido um objeto.
p1 = Pessoa('Ana', 123456)
print(p1.nome)
print(p1.__cpf)  #Erro
print(p1.mostrar())  # Aqui é o modo mais recomendado da OOP para demonstração de atributos privados.

"""
Encapsulamento:
    Tipos de atributos:
        1 - Publicos
            É só não adicionar nada no atributo
            
        2 - Privado
            Basta adicionar "__" (sem as aspas) no inicio do nome do atributo
            
        3 - protegido
            Basta adicionar "_" (sem as aspas) no inicio do nome do atributo
    
    Os métodos também podem ser públicos ou privados:
        Privados:
            Basta adicionar "__" (sem as aspas) no inicio do nome do método
    
      
    Cuidado: Métodos que acessam diretamente atributos não podem ser públicos.
"""
