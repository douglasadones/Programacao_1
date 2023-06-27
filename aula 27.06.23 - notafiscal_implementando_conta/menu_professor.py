from random import randint
from conta import Conta


def pesquisar_conta(contas, numero):
    for i, conta in enumerate(contas):
        if conta.get_numero() == numero:
            return contas[i]


def menu():
    while True:
        print("\n############ MENU PRINCIPAL ############")
        print("1. Criar Conta      2. Mostrar Saldo")
        print("3. Depósitar        4. Sacar Valor")
        print("5. Transferência    6. Extrato da Conta")
        print("0. Sair")
        print("---------------------------------------")
        op = int(input("Digite sua opção -> "))
        if 0 <= op <= 6:
            return op
        else:
            print("---------------")
            print("Opção inválida!")
            print("---------------")
            continue


def principal():
    contas = []
    while True:
        op = menu()
        if op == 0:
            break
        elif op == 1:
            print("#### CRIANDO UMA CONTA ####")
            numero = randint(1000, 9999)
            titular = input("Nome do cliente: ").upper()
            try:
                valor = float(input("Saldo inicial: "))
            except:
                print("Valor inválido!")
                print("Criando conta com saldo: R$ 0.00")
                valor = 0.00
            else:
                contas.append(Conta(numero, valor, titular))
                contas[-1].mostrar_saldo()
                print(f"Conta {numero} criada com sucesso!")
        elif op == 2:
            print("##### SALDO EM CONTA #####")
            num = int(input("Número da conta: "))
            conta = pesquisar_conta(contas, num)
            if conta:
                conta.mostrar_saldo()
        elif op == 3:
            print("#### DEPÓSITO EM CONTA ####")
            num = int(input("Número da conta: "))
            try:
                valor = float(input("Valor a depositar: "))
            except:
                print("Valor inválido!")
            else:
                conta = pesquisar_conta(contas, num)
                if conta:
                    conta.depositar(valor)
        elif op == 4:
            print("##### SAQUE EM CONTA #####")
            num = int(input("Número da conta: "))
            try:
                valor = float(input("Valor a sacar: "))
            except:
                print("Valor inválido!")
            else:
                conta = pesquisar_conta(contas, num)
                if conta:
                    if conta.sacar(valor):
                        print("Saque realizado com sucesso!")
        elif op == 5:
            print("### TRANSFERÊNCIA ENTRE CONTAS ###")
            num1 = int(input("Número da conta de origem: "))
            num2 = int(input("Número da conta de destino: "))
            try:
                valor = float(input("Valor a transferir: "))
            except:
                print("Valor inválido!")
            else:
                conta1 = pesquisar_conta(contas, num1)
                conta2 = pesquisar_conta(contas, num2)
                if conta1 and conta2:
                    if conta1.transferir(conta2, valor):
                        print("Transferência realizada com sucesso!")
        elif op == 6:
            print("#### EXTRATO DE CONTA ####")
            num = int(input("Número da conta: "))
            conta = pesquisar_conta(contas, num)
            if conta:
                conta.extrato()
        else:
            print("\n##### OPÇÃO INVÁLIDA #####\n")


if __name__ == "__main__":
    principal()
