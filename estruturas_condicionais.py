MAIOR_IDADE = 18
IDADE_ESPECIAL = 12

idade = int(input("Informe idade:"))

if idade >= MAIOR_IDADE:
    print("Maior de idade, pode tirar CNH")

if idade < MAIOR_IDADE:
    print("Menor não pode!")

if idade >= MAIOR_IDADE:
    print("Maior de idade, pode tirar CNH")
elif idade >= IDADE_ESPECIAL:
    print("Só aulinha,  bebê!")
else:
    print("Menor rapaz, não pode!")
