
saldo = 2000
saque = 2100
cheque_especial = 450

status = "Sucesso" if saldo >= saque else "Falha"

print(f"{status} ao realizar o saque")