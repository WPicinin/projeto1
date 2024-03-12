saldo = 0
extrato = 0
limite_saque = 3

menu = ("""
        
 [1] Depositar
 [2] Sacar
 [3] Extrato
 [4] Sair
        
""")

while True:

    opcao = input(menu)

    if opcao == "1":
        valor = float(input("escolha o valor para depositar: "))
        if valor > 0:
            saldo += valor
            extrato = saldo
            print("foram depositados", valor,
                  "reais, a sua conta agora tem R$", extrato)
        else:
            print("Valor inválido, tente novamente")

    elif opcao == "2":

        if limite_saque > 0:
            valor = float(input("escolha o valor para sacar: "))
            if valor < saldo:
                saldo -= valor
                print("A sua conta agora tem R$", saldo)
                limite_saque = limite_saque-1
                print("Você tem", limite_saque, "de saques restante")
            else:
                print("Você não tem saldo suficiente, tente novamente")

        else:
            print("Você antingiu o máximo de saques diários")

    elif opcao == "3":
        print("Extrato: R$", saldo)

    elif opcao == "4":
        print("Até logo...")
        break
    else:
        print("opção inválida")
