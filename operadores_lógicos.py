saldo = 1000
saque = 250
limite = 200
conta_especial = True

## print(True and True)
## print(True and False)
## print(False and False)
## print(True or False)
## print(True or True)
## print(False or False)

# AND - PARA SER TRUE TUDO TEM QUE SER TRUE
# OU - APENAS UM TEM QUE SER TRUE


exp = saldo >= saque and saque <= limite or conta_especial and saldo >=saque

print(exp)

exp_2 = (saldo >= saque and saque <= limite) or (conta_especial and saldo >=saque)

print(exp_2)

## MELHOR QUEBRAR O CODIGO PARA FICAR MAIS LEGIVEL
conta_normal_com_saldo_suficiente = (saldo >= saque and saque <= limite)
conta_expecial_com_saldo_suficiente = (conta_especial and saldo >=saque)

exp_3 = conta_expecial_com_saldo_suficiente or conta_normal_com_saldo_suficiente

print(exp_3)

