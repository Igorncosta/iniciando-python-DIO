texto = input("Digite seu tweet: ")

# Verificando o comprimento do texto
if len(texto) <= 140:
    print(texto)
else:
    print("MUTE")
    
