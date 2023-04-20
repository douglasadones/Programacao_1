contas = dict()


def gerar_conta(titular, valor):
    conta = [titular, valor]
    return conta


def emitir_relatorio(contas):
    for num in contas:
        print(f"Número: {num}")


def menu_principal():
    numero = 0
    while True:
        print("""\n############# MENU PRINCIPAL #############
        1. Criar conta      2. mostrar saldo
        3. deposito         4. saque
        5. transferencia    6. relatório geral
        0. sair
        -----------------------------------------""")
        op = int(input("Digite a sua opção -> "))
        if op == 0:
            break
        elif op == 1:
            print("#### CRIANDO UMA CONTA ####")
            numero += 1
            titular = input("Nome do cliente: ")
            valor = float(input("Saldo Inicial: "))
            contas[numero] = gerar_conta(titular, valor)
        elif op == 6:
            print("## EMITIR RELATORIO")
