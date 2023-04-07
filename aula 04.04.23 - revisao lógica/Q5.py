"""Crie um script que ler três números e mostre‐os em ordem decrescente."""

n1, n2, n3 = int(input("")), int(input("")), int(input(""))

if n1 > n2 and n1 > n3:
    print(n1, end=" ")
    if (n2 > n3):
        print(n2, n3)
    else:
        print(n3, n2)
if n2 > n3:
    print(n2, end=" ")
    if n1 > n3:
        print(n1, n3)
    else:
        print(n3, n1)
else:
    print(n3, end=" ")
    if n1 > n2:
        print(n1, n2)
    else:
        print(n2, n1)
