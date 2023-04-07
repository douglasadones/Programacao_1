"""Crie um script que pergunte o preço de três produtos e informe qual o produto você deve comprar, sabendo que a decisão
é sempre pelo mais barato"""

p1, p2, p3 = int(input()), int(input()), int(input())

if p1 < p2 and p1 < p3:
    print(p1)
elif p2 < p3:
    print(p2)
else:
    print(p3)


# ou podemos seguir essa lógica:
p1, p2 = int(input()), int(input())
menor = 0
if p1 < p2:
    menor = p1
else:
    menor = p2
p3 = int(input())
if p3 < menor:
    menor = p3
print(menor)

# Ou assim:

p1, p2 = int(input()), int(input())
menor = 0
if p2 < p1:
    p1, p2 = p2, p1
p3 = int(input())
if p3 < p1:
    p1, p3 = p3, p1
print(p1)
