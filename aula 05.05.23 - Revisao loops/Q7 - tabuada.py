"""Faça o algoritmo de imprimir a tabuada de um número fornecido pelo usuário, usando
while. Após mostrar a tabuada o programa deve perguntar se deseja imprimir a tabuada de um novo
número."""

continuar = 1
while continuar:
    num = int(input("Informe um número: "))
    for c in range(1, 11):
        print(f"{num} + {c:>2} = {(num + c):>2}", end=" | ")
        print(f"{num} - {c:>2} = {(num - c):>2}", end=" | ")
        print(f"{num} x {c:>2} = {(num * c):>2}", end=" | ")
        print(f"{num} / {c:>2} = {(num / c):.1f}")
    continuar = int(input("Deseja imprimir a tabuada de um novo número? (0 para não e 1 para sim): "))
