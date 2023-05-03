from random import randrange


def gravar(lista, arq):
    arquivo = open(arq, "w")
    for fruta in lista:
        arquivo.write(fruta + "\n")
    arquivo.close()


def ler(arq):
    lista = []
    arquivo = open(arq, "r")
    for fruta in arquivo:
        lista.append(fruta)
    arquivo.close()
    return lista


def mostrar(frutas):
    for fruta in frutas:
        fruta = fruta.strip()
        print(fruta, end=" ")
    print("")


def jogar(palavra_secreta):
    letras_acertadas = ['_' for letra in palavra_secreta]
    print(f"Palavra: {palavra_secreta}")
    erros = 0
    while True:
        print(f"Cifra..: {letras_acertadas}")
        chute = input("Letra: ").upper().strip()
        if chute in palavra_secreta:
            for i, letra in enumerate(palavra_secreta):
                if chute == palavra_secreta[i]:
                    letras_acertadas[i] = palavra_secreta[i]
            if palavra_secreta == "".join(letras_acertadas):
                print(f"Palavra Secreta: {palavra_secreta}")
                print("Parabens, você acertou!")
                break
        else:
            erros += 1
            print(f"Erro: {erros}")
            if erros >= 6:
                print("Você perdeu!!")


def main():
    lista = ["banana", "melancia", "laranja", "manga", "tangerina"]
    gravar(lista, "palavras.txt")
    frutas = ler("palavras.txt")
    numero = randrange(0, len(frutas))
    palavra_secreta = frutas[numero].upper().strip()
    jogar(palavra_secreta)


if __name__ == "__main__":
    main()
