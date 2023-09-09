conta = {"cpf":"", "nroConta":"", "saldo":""}
cont = int(input("Quantas contas deseja cadastrar? "))
i = 0
while i < cont:
    cpf = input("Informe o CPF do cliente: ")
    nroConta = input("Informe o nro da conta: ")
    saldo = float(input("Informe o saldo da conta: "))
    conta["cpf"] = cpf
    conta['nroConta'] = nroConta
    conta["saldo"] = saldo
    i += 1

for contaLista in conta.items():
    print(contaLista)