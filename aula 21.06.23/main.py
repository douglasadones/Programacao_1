from conta import Conta
from random import randint
contas = [Conta(randint(1000, 9999), 1000.00, f"Titular{c}")for c in range(5)]
#
# for c in contas:
#     print(c.saldo, c.numero, c.titular)
#     print()
#
# print(contas[0].numero, contas[0].sacar(200), contas[0].extrato())

menu = """CONTA BANCARIA
1. Contas existentes
2. Sacar
3. Depositar
4. Mostrar Saldo
5. Extrato
6. Criar conta
7. Transferir
0. Sair"""

while True:
    print(menu)
    escolha = int(input("Sua escolha: "))

    if escolha == 0:
        break

    if escolha == 1:
        contador = 0
        for c in contas:
            print(f'Conta{contador}: {c.titular}, Número: {c.numero}, Saldo: {c.saldo}')
            contador += 1
        conta_atual = int(input("Informe a Conta que deseja usar: Conta"))
        conta = contas[conta_atual]

    elif escolha == 2:
        valor = float(input('Informe o valor a ser sacado: '))
        if valor <= conta.saldo:
            conta.sacar(valor)
            print("Operação concluída com sucesso!")

    elif escolha == 3:
        valor = float(input('Informe o valor a ser depositado: '))
        status = conta.depositar(valor)
        if status:
            print("Operação Realizada com sucesso!")

    elif escolha == 4:
        conta.mostrar_saldo()

    elif escolha == 5:
        conta.extrato()

    elif escolha == 6:
        numero = int(input("Número: "))
        saldo = float(input("Saldo: "))
        titular = str(input("Titular: "))
        conta = Conta(numero, saldo, titular)

    elif escolha == 7:
        conta_destino = int(input('Conta destino: Conta'))
        valor = float(input('Informe o Valor da transferência: '))
        conta.transferir(conta, contas[conta_destino], valor)

    else:
        pass
