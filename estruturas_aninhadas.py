conta_normal = False
conta_universitaria = False

saldo = 2000
saque = 100
cheque_especial = 450


if conta_normal:
    if saldo >= saque:
        print("Saque realizado com sucesso!")
    elif saque <= (saldo + cheque_especial):
        print("Saque utilizando cheque especial!")
    else:
        print("Saldo insuficiente!")
        #### TUDO QUE ESTA AQUI DENTRO SE REFERE SE É CONTA NORMAL. NADA ALEM DE CONTA NORMAL

elif conta_universitaria:
    if saldo >= saque:
        print("Saque realizado com sucesso!")
    else:
        print("Saldo insuficiente!")
        #### TUDO QUE ESTA AQUI DENTRO SE REFERE SE É CONTA UNIVERSITARIA. NADA ALEM DE CONTA UNIVERSITARIA

#### JA FORA SO "SE: NORMAL / SENAO UNIVERSITARIA"TEM A CONTA "IGAO", QUE NÃO É NENHUMA NEM OUTRA:"
else:
    print("Sua conta pode sacar quanto quiser papai!")