texto = input("Informe seu texto:")
VOGAIS = "AEIOU"

# EXEMPLO USANDO ITERAÇÃO
for letra in texto:
    if letra.upper() in VOGAIS:
        print(letra, end="  ")
else:
    print()
    
# EXEMPLO UTILIZANDO A FUNÇÃO BUILT-IN RANGE
for numero in range(0, 51, 5):
    print(numero, end=" ")