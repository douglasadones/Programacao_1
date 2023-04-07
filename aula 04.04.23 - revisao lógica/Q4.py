""" Crie um script que leia um número inteiro (4 dígitos) referente a um ano e
determine se o mesmo e ou não um ano bissexto (divisível por 4).Os anos bissextos são:
divisíveis por 4 e não divisíveis por 100; ou divisíveis por 400."""

ano = int(input(""))

if ano % 400 == 0:
    print("É ano bissexto")
elif ano % 4 == 0 and ano % 100 != 0:
    print("É ano bissexto")
else:
    print("Não é Ano Bissexto")
