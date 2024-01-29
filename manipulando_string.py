nome = "Igor"

print(nome.upper()) #NOME MAIUSCULO
print(nome.lower()) # nome minusculo
print(nome.title()) # Só o Inicial

texto = "  Olá mundo!    "

print(texto)
print(texto.strip() + ".") # remover espaços
print(texto.rstrip() + ".") # remover espaços direita
print(texto.lstrip() + ".") # remover espaços esquerda

menu = "Pyhton"

print("####" + menu + "####")
print(menu.center(14, "#")) # CENTRALIZA COM O DETERMINADO NUMERO DE CARACTER
print("-".join(menu)) # COLOCA UM CARACTER ENTRE AS LETRAS