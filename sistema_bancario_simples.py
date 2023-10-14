menu = """

[1] Depositar
[2] Sacar
[3] Extrato
[4] Sair

=> """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3
utilizou_sistema = False

while True:

    opcao = input(menu)

    if opcao == "1":
        valor = float(input("Informe o valor do depósito: "))
        utilizou_sistema = True

        if valor > 0:
            saldo += valor
            extrato += f"Depósito: R$ {valor:.2f}\n"
            
        else:
            print("Não foi possível realizar o depósito. O valor informado é inválido!")

    elif opcao == "2":
        valor = float(input("Informe o valor do saque: "))
        utilizou_sistema = True

        excedeu_saldo = valor > saldo

        excedeu_limite = valor > limite

        excedeu_saque = numero_saques >= LIMITE_SAQUES

        if excedeu_saldo:
            print("Operação falhou! Você não tem saldo suficiente.")

        elif excedeu_limite:
            print("Operação falhou! O valor do saque excede o limite.")

        elif excedeu_saque:
            print("Operação falhou! Número máximo de saques excedido.")

        elif valor > 0:
            saldo -= valor
            extrato += f"Saque: R$ {valor:.2f}\n"
            numero_saques += 1

        else:
            print("Operação falhou! O valor informado é inválido.")

    elif opcao == "3":

        if utilizou_sistema == False:
            print("\n############# Extrato #############")
            print("\n")
            print("Não foram realizadas movimentações.")
            print(f"\nSaldo: R$ {saldo:.2f}")
            print("\n")
            print("####################################")

        elif utilizou_sistema == True:
            print("\n############# Extrato #############")
            print("\n")
            print(f"\nSaldo: R$ {saldo:.2f}")
            print("\n")
            print("####################################")

    elif opcao == "4":
        break

    else:
        print("Operação inválida, por favor selecione novamente a opção desejada.")
