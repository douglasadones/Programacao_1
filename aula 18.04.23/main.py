import math
print(math)
"""
if __name__ = "__main__":
    main()

Essa estrutura normalmente é adicionada dentro do arquivo com módulos, por exemplo: math
Ex:
    Digamos que no final do "math.py", exista:
        print("testando o print fora do if __main__")
    E depois:
        if __name__ = "__main__":
            print("testando o print dentro do if")
            
se nesse arquivo eu adicionar:
    import math
    print("math")
será printado:
    testando o print fora do if __main__
    <module 'math' (built-in)>

agora se rodar o arquivo "math.py":                
            

############# MENU PRINCIPAL #############
1. Criar conta      2. mostrar saldo
3. deposito         4. saque
5. transferencia    6. relatório geral
0. sair
------------------------------------------

UI DE CADA OPÇÃO:
Ex: ########## SALDO EM CONTA ##########
"""
try:
    n = float(input(""))
except Exception as erro:
    print(f"Erro encontrado: ({erro})")
else:
    print("Teste")
finally:
    print("Teste 2")
