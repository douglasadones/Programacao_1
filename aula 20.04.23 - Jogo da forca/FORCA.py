while True:
    op = int(input("""1. Jogar\n2. Cadastrar Palavras\n3. Resetar Arquivos\n0. Sair do Programa\nOpção: """))

    if op == 1:
        pass
    elif op == 2:
        file = open('palavras.txt', 'a')
        while True:
            palavra = input("Palavra (Para sair digite enter): ")
            if palavra == "":
                break
            file.write(palavra + "\n")
        file.close()
    elif op == 3:
        file = open('palavras.txt', 'w')
    elif op == 0:
        break
    else:
        print('Opçõa Inválida')

