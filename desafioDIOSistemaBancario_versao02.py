import textwrap

def menu():
    menu = """ \n
    ==== Sistema Bancário ====
    [ D ] Depositar
    [ S ] Sacar
    [ E ] Extrato
    [ U ] Novo Cliente
    [ AC ] Nova Conta
    [ L ] Lista Clientes
    [ LC ] Lista Contas
    [ Q ] Sair
    => """
    return input(textwrap.dedent(menu)).upper()

def CadastrarCliente(clientes):
    cpf = input("Informe o CPf do cliente: ")
    cliente = filtrar_cliente(cpf, clientes)

    if cliente:
        print("Cliente já cadastrado!")
        return
    
    nome = input("Informe o nome do cliente: ").upper()
    data_nascimento = input("Informe a data de nascimento: ")
    endereco = input("Informe o endereço do cliente: ").upper()

    clientes.append({"nome":nome, "dataDeNascimento": data_nascimento, "cpf":cpf, "endereco":endereco})

    print("Cliente cadastrado com sucesso!")

def filtrar_cliente(cpf, clientes):
    clientes_filtrados = [clientes for cliente in clientes if cliente["cpf"]== cpf]
    return clientes_filtrados[0] if clientes_filtrados else None
    

def AbrirConta(agencia, nro_conta, clientes):
    cpf = input("Informe o CPf do cliente: ")
    cliente = filtrar_cliente(cpf, clientes)

    if cliente:
        print("Conta aberta com sucesso!")
        return {"agencia": agencia, "nro_conta":nro_conta, "cliente":cliente}
    
    print("Cliente não localizado. Conta não pode ser aberta!")

def ListarClientes(clientes):
    for cliente in clientes:
        print("Nome: ", cliente["nome"])
        print("Endereço: ", cliente["endereco"])

def ListarContas(contas):
    for conta in contas:
        linha = f"""
            Agência:\t{conta['agencia']}
            C/C: \t\t{conta['nro_conta']}
            Titular:\t{conta['cliente']}
        """
        print("*" * 100)
        print(textwrap.dedent(linha))

def Depositar(saldo, valor, extrato, /):
    while valor <= 0:
        print("Valor de depósito inválido! Favor depositar valor maior que zero.")
        valor = float(input("Informe o valor a ser depositado: "))
    
    saldoAnterior = saldo
    saldo += valor
    entradaExtrato = f"""
    Saldo anterior: R$ {saldoAnterior:.2f}.
    Depósito: R$ {valor:.2f}.
    Saldo atual: R$ {saldo:.2f}.
    """
    extrato += entradaExtrato

    return saldo, extrato

def ExibirExtrato(saldo, /, *, extrato):
    print("========== Exibir extrato ========")
    print("Não foram realizadas movimentações." if not extrato else extrato)
    print(f"\nSaldo consolidado:\t\tR$ {saldo:.2f}")
    print("================================")

def EfetuarSaque(*, saldo, valor, extrato, limite, nro_saques, limite_saques):
    excedeu_saldo = valor > saldo
    excedeu_limite = valor > limite
    excedeu_saques = nro_saques > limite_saques

    if excedeu_saldo:
        print("Saque não realizado. Saldo insuficiente!")
    elif excedeu_limite:
        print("Saque não realizado. Valor de saque excede o limite perimtido.")
    elif excedeu_saques:
        print("Saque não realizado. Número máximo de saques excedido.")
    elif valor > 0:
        saldoAnterior = saldo
        saldo -= valor
        nro_saques += 1
        entradaExtrato = f"""
        Saldo anterior: R$ {saldoAnterior:.2f}.
        Saque: R$ {valor:.2f}.
        Saldo atual: R$ {saldo:.2f}.
        """
        extrato += entradaExtrato
    else:
        print("Saque nao realizado. Valor informado inválido!")
    
    return saldo, extrato, nro_saques

def main():
    saldo = 0
    limite = 500
    extrato = ""
    nro_saques = 0
    LIMITE_SAQUES = 3
    AGENCIA = "0001"
    contas = []
    clientes = []
    
    while True:
        opcao = menu()

        if opcao == "D":
            print("Realizar depósito")
            valorDeposito = float(input("Informe o valor a ser depositado: "))
            saldo, extrato = Depositar(saldo, valorDeposito, extrato)

        elif opcao == "S":
            print("Realizar saque")
            valorSacado = float(input("Informe o valor a ser sacado: "))
            saldo, extrato, nro_saques = EfetuarSaque(saldo = saldo,
                                          valor = valorSacado, 
                                          extrato = extrato,
                                          limite = limite,
                                          nro_saques = nro_saques,
                                          limite_saques = LIMITE_SAQUES,
                                          )
            
        elif opcao == "E":
            ExibirExtrato(saldo, extrato = extrato)

        elif opcao == "U":
            CadastrarCliente(clientes)

        elif opcao == "L":
            ListarClientes(clientes)

        elif opcao =="AC":
            nro_conta = len(contas) + 1
            conta = AbrirConta(AGENCIA, nro_conta, clientes)

            if conta:
                contas.append(conta)

        elif opcao =="LC":
            ListarContas(contas)

        elif opcao =="Q":
            break
    else:
        print("Opção inválida!")

main()
