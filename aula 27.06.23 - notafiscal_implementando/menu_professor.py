from random import randint
from conta import Conta
from cliente import Cliente
from agencia import Agencia


def pesquisar_conta(contas, numero):
    for i, conta in enumerate(contas):
        if conta.get_numero() == numero:
            return contas[i]


def pesquisar_agencia(agencias, numero):
    for i, agencia in enumerate(agencias):
        if agencia.get_numero() == numero:
            return agencias[i]


# Falta criar uma forma de procurar as contas em uma agência


def menu():
    while True:
        print("\n############ MENU PRINCIPAL ############")
        print("1. Cadastrar Agencia        2. Mostrar Agencias")
        print("2. Mostrar Contas existentes 3. Criar conta")
        print("4. Criar Conta               5. Mostrar Saldo")
        print("6. Depósitar                 7. Sacar Valor")
        print("8. Transferência             9. Extrato da Conta")
        print("10. Informações do cliente   0. Sair")
        print("---------------------------------------")
        op = int(input("Digite sua opção -> "))
        if 0 <= op <= 10:
            return op
        else:
            print("---------------")
            print("Opção inválida!")
            print("---------------")
            continue


def principal():
    contas = []
    agencias = []
    while True:
        op = menu()
        if op == 0:
            break
        elif op == 1:
            print("#### CADASTRANDO UMA AGENCIA ####")
            numero = randint(1000, 9999)
            nome = input("Nome da agencia: ").upper()
            cidade = input("Informe a cidade: ")
            uf = input("informe o uf: ")
            enderecos = []
            c = 1
            while True:
                print("Informe seu(s) endereço(s) - (enter para encerrar)")
                endereco = input(f'{c}º Endereço: ')
                if endereco == "":
                    break
                else:
                    enderecos.append(endereco)
                    c += 1
            a1 = Agencia(nome, cidade, uf)
            a1.set_numero(numero)
            for c in enderecos:
                a1.set_endereco(c)
            agencias.append(a1)
            print(f"Agencia {numero} Cadastrada com sucesso!")

        elif op == 2:
            if len(agencias) == 0:
                print('----- NENHUMA AGENCIA CADASTRADA -----')
            else:
               print("------- AGENCIAS CADASTRADAS -------")
               for c in agencias:
                   print(f"Nome da agencia: {c.get_numero()}")

        elif op == 3:
            print("#### CONTAS CADASTRADAS ####")
            ag = int(input("Número da Agencia: "))
            co = int(input("Número da Conta: "))
            agencia = pesquisar_conta(agencias, ag)
            conta = pesquisar_conta(contas, co)
            if agencia and conta:
                conta.mostrar_saldo()
            else:
                if not agencia and not conta:
                    print('Agencia e conta Inexistente')
                elif not agencia:
                    print('Agencia Inexistente!')
                else:
                    print('Conta Inexistente!')

        elif op == 4:
            print("#### CRIANDO UMA CONTA ####")
            numero = randint(1000, 9999)
            titular = input("Nome do cliente: ").upper()
            print("#### SOBRE O CLIENTE ####")
            cpf = int(input('Informe o CPF: '))
            cidade = input("Informe a cidade: ")
            uf = input("informe o uf: ")
            enderecos = []
            c = 1
            while True:
                print("Informe seu(s) endereço(s) - (enter para encerrar)")
                endereco = input(f'{c}º Endereço: ')
                if endereco == "":
                    break
                else:
                    enderecos.append(endereco)
                    c += 1
            print("Cadastro Realizado com sucesso!")
            try:
                valor = float(input("Saldo inicial: "))
            except:
                print("Valor inválido!")
                print("Criando conta com saldo: R$ 0.00")
                valor = 0.00
            else:
                contas.append(Conta(numero, valor, titular))
                c1 = Cliente(cpf, titular, cidade, uf)
                for c in enderecos:
                    c1.set_endereco(c)
                contas[-1].set_cliente(c1)
                contas[-1].mostrar_saldo()
                print(f"Conta {numero} criada com sucesso!")
        elif op == 5:
            print("##### SALDO EM CONTA #####")
            ag = int(input("Número da Agencia: "))
            co = int(input("Número da Conta: "))
            agencia = pesquisar_conta(agencias, ag)
            conta = pesquisar_conta(contas, co)
            if agencia and conta:
                conta.mostrar_saldo()
            else:
                if not agencia and not conta:
                    print('Agencia e conta Inexistente')
                elif not agencia:
                    print('Agencia Inexistente!')
                else:
                    print('Conta Inexistente!')
        elif op == 6:
            print("#### DEPÓSITO EM CONTA ####")
            ag = int(input("Número da Agencia: "))
            co = int(input("Número da Conta: "))
            agencia = pesquisar_conta(agencias, ag)
            conta = pesquisar_conta(contas, co)
            if agencia and conta:
                num = int(input("Número da conta: "))
                try:
                    valor = float(input("Valor a depositar: "))
                except:
                    print("Valor inválido!")
                else:
                    conta = pesquisar_conta(contas, num)
                    if conta:
                        conta.depositar(valor)
            else:
                if not agencia and not conta:
                    print('Agencia e conta Inexistente')
                elif not agencia:
                    print('Agencia Inexistente!')
                else:
                    print('Conta Inexistente!')
        elif op == 7:
            print("##### SAQUE EM CONTA #####")
            ag = int(input("Número da Agencia: "))
            co = int(input("Número da Conta: "))
            agencia = pesquisar_conta(agencias, ag)
            conta = pesquisar_conta(contas, co)
            if agencia and conta:
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
            else:
                if not agencia and not conta:
                    print('Agencia e conta Inexistente')
                elif not agencia:
                    print('Agencia Inexistente!')
                else:
                    print('Conta Inexistente!')

        elif op == 8:
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
        elif op == 9:
            print("#### EXTRATO DE CONTA ####")
            num = int(input("Número da conta: "))
            conta = pesquisar_conta(contas, num)
            if conta:
                conta.extrato()
        elif op == 10:
            print("##### INFORMAÇÕES DO CLIENTE #####")
            num = int(input("Número da conta: "))
            conta = pesquisar_conta(contas, num)
            if conta:
                conta.info_cliente()
        else:
            print("\n##### OPÇÃO INVÁLIDA #####\n")


if __name__ == "__main__":
    principal()
