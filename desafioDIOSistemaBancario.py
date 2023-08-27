menu = """
==== Sistema Bancário ====
[ D ] Depositar
[ S ] Sacar
[ E ] Extrato
[ Q ] Sair
=> 
"""

saldo = 0 
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:

    opcao = input(menu).upper()

    if opcao == "D":
        print("Realizar depósito")
        valorDeposito = float(input("Informe o valor a ser depositado: "))
        while valorDeposito <=0:
            print("Valor de depósito inválido! Favor depositar valor maior que zero.")
            valorDeposito = float(input("Informe o valor a ser depositado: "))
        saldoAnterior = saldo
        saldo += valorDeposito
        entradaExtrato = f"""
        Saldo anterior: R$ {saldoAnterior:.2f}.
        Depósito: R$ {valorDeposito:.2f}.
        Saldo atual: R$ {saldo:.2f}.
        """
        extrato += entradaExtrato
    
    elif opcao == "S":
        while numero_saques < LIMITE_SAQUES:
            print("Realizar saque")
            valorSacado = float(input("Informe o valor a ser sacado: "))
            while valorSacado > saldo or valorSacado > 500:
                print("Saque não permitido. Valor acima do saldo na conta ou acima do limite de R$ 500,00!")
                valorSacado = float(input("Informe o valor a ser sacado: "))
        
            saldoAnterior = saldo
            saldo -= valorSacado
            entradaExtrato = f"""
            Saldo anterior: R$ {saldoAnterior:.2f}.
            Saque: R$ {valorSacado:.2f}.
            Saldo atual: R$ {saldo:.2f}.
            """
            extrato += entradaExtrato

            numero_saques += 1
            print("Resta(m): ", 3 - numero_saques, "saque(s)")
            break
        else: print("Limite de saques diários atingido.")
    
    elif opcao == "E":
        print("==========Exibir extrato========")
        print(extrato)
        print("================================")
    elif opcao =="Q":
        break
    else:
        print("Opção inválida!")
