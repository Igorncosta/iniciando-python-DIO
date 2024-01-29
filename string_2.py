nome = "Igor"
idade = 30
saldo = 1457.255


print("Nome: %s Idade %d" % (nome, idade)) ## metodo % de formatar

print("Nome: {} Idade {}".format(nome,idade)) #Metodo format {} de formatar

print("Nome: {0} Idade {1}".format(nome,idade)) #Metodo format  {} de formatar
print("Nome: {1} Idade {0}".format(idade,nome)) #Metodo format  {} de formatar

print("Nome: {name} Idade {age}".format(name=nome, age=idade)) #Metodo format  {} de formatar


print(f"Nome: {nome} Idade {idade}") # Método f-string
print(f"Nome: {nome} Idade {idade} Saldo: {saldo:.2f}") # Método f-string formatando float no saldo