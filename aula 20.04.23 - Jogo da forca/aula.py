#
# try:
#     num = int(input(''))
# except Exception as erro:
#     print(f"Ocorreu a exceção: {erro.__cause__}")


"""

NameError -> Variável não declarada
ModuleNotFoundError
EOFError -> Final de um arquivo
AttributeError -> Método ou método inexistente


"""

# try:
#     num = int(input())
# except (NameError, KeyboardInterrupt, ValueError) as erro:
#     print(erro)

letra = 'abaabbbaaaabbaab'

letra = '-'.join(letra)
letra = letra.split('-')
print(letra)
