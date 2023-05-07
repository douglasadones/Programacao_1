# TODO a) - crie/abra um arquivo texto de nome ”arq.txt”
try:
    file = open('arq.txt', 'r')
    file.close()
except:
    file = open('arq.txt', 'w')
    file.close()

# TODO - b) permita que o usuário entre com diversos caracteres nesse arquivo, até que o usuário entre com o
#  caractere ‘0’ [zero];

with open('arq.txt', 'a') as file:
    while True:
        caractere = input('Informe os caracteres ("0" para terminar): ').strip()
        if caractere != '0':
            file.write(caractere + '\n')
        else:
            break

# TODO - reinicie o arquivo, fazendo o stream apontar para seu início;
with open('arq.txt', 'r') as file:
    # TODO - d) lendo-o caractere por caractere, e escrevendo na tela todos os caracteres armazenados.
    for linha in file:
        print()
        for caractere in linha:
            print(caractere, end=' ')
