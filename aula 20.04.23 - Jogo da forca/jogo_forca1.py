from random import randint

while True:
    file = 0
    print("===================================")
    print("### MENU PRINCIPAL ###")
    print("1. Jogar")
    print("2. Cadastrar Palavras")
    print("3. Resetar Arquivo")
    print("0. Sair do Programa")
    op = int(input("Opção: "))
    if op == 1:
        erro = 0
        try:
            file = open("palavras.txt", "r")
        except:
            print("===================================")
            print("Arquivo de palavras não encontrado!")
            print("Tente cadastrar palavras antes...")
            continue
        arquivo = file.read().split()
        palavra = arquivo[randint(0, len(arquivo)-1)]
        print(palavra)
        lista = "_ " * len(palavra)
        lista = lista.split()
        while erro < 6:
            print(f"Palavra: {''.join(lista)}")
            letra = input("Letra: ").upper().strip()
            if letra in palavra:
                for i, ch in enumerate(palavra):
                    if ch == letra:
                        lista[i] = ch
                if "_" not in lista:
                    print("===================================")
                    print(f"Palavra: {''.join(lista)}")
                    print("PARABÉNS, você venceu!!")
                    input("Tecle ENTER para continuar... ")
                    break
            else:
                erro += 1
                print(f"Erro: {erro}")
                if erro == 6:
                    print("Você perdeu!!")
    elif op == 2:
        file = open("palavras.txt", "a")
        while True:
            print("Para Sair, apenas tecle ENTER")
            palavra = input("Palavra: ").upper().strip()
            if palavra == "":
                break
            file.write(palavra + "\n")
        file.close()
    elif op == 3:
        file = open("palavras.txt", "w")
        print("Dados removidos!")
    elif op == 0:
        break
    else:
        print("Opção Inválida!!")
