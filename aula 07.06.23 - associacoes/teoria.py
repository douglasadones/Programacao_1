"""
prova dia 15

Relacionamentos entre objetos --------------------------------------------

- Associoação:
    "Ambos existem mas não dependem um do outro"

- Agragação
    "Ambos podem existir separadas mas funcionaria de forma "frustrada"

        Ex:
            Carro  --> é o todo
            Pneu, Motor --> Parte

             O carro, sem pneu e motor, ainda existe, mas não funcionará completamente.

- Composição
    Todo:
        Se o todo não existir, a parte não existirá
    Parte:
        Não tem finalidade, se não, participar do todo

    Ex:
        Sistema de vendas em uma loja online:
            Todo:
                Cliente da loja
                Parte do cliente: (Parte de um todo)
                    Endereço do cliente


    Representação:
    |Classe1| -------------------|Classe2| : Associação
    |Classe1| ------------------°|Classe2| : Agregação
    |Classe1| ------------------.|Classe2| : Composição

- Herança


"""
