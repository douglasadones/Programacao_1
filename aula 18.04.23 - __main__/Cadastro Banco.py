def sacar(conta, valor):
    conta['saldo'] -= valor


def depositar(conta, valor):
    conta['saldo'] += valor


def transferencia(conta_a_transferir, conta_a_receber, valor_da_transferencia):
    sacar(conta_a_transferir, valor_da_transferencia)
    depositar(conta_a_receber, valor_da_transferencia)


def localizacao_conta(num_conta):
    for cadastro in todos_os_cadastros:
        if cadastro['conta'] == num_conta:
            print(cadastro)
            return cadastro


todos_os_cadastros = []
while True:
    print("""\n############# MENU PRINCIPAL #############
    1. Criar conta      2. mostrar saldo
    3. deposito         4. saque
    5. transferencia    6. relatório geral
    0. sair
    -----------------------------------------""")
    escolha = int(input("Digite a sua opção -> "))
    if escolha == 0:
        break
    else:
        num_conta = int(input("informe o número da conta: "))
        conta = localizacao_conta(num_conta)
    if escolha == 1:
        dict = {}
        nome = input("Informe o nome do titular: ").title()
        saldo_inicial = float(input("Informe o saldo inicial: "))
        dict['conta'] = num_conta
        dict['nome'] = nome
        dict['saldo'] = saldo_inicial
        todos_os_cadastros.append(dict.copy())
    elif escolha == 2:
        print(f"Saldo atual de {conta['nome']}: R$ {conta['saldo']}")
    elif escolha == 3:
        valor = float(input("Informe o valor a ser depositado: "))
        depositar(conta, valor)
    elif escolha == 4:
        saque = float(input("Informe o valor a ser sacado: "))
        sacar(conta, saque)
    elif escolha == 5:
        valor = float(input("Informe o valor da transferência: "))
        conta_para_receber = int(input("Informe o número da conta que irá receber: "))
        receber = localizacao_conta(conta_para_receber)
        transferencia(conta, receber, valor)
