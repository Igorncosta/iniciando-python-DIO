while True:
    numero = int(input("Escolha: "))

    if numero == 10:
        break

    print(numero)
    ## O BREAK VAI FUNCIONAR ATE O NUMERO SER ATINGINDO. OU SEJA, VAI FICAR EM LOOP INFINITO ATE ATINGIR O NUMERO "10".
        ## ELE CORTA O LAÇO DE REPETIÇÃO SE O NUMERO FOR "10"
    
    ## EXISTE O "CONTINUE" TBM POREM ELE USA PARA NAO EXIBIR O NUMERO QUE DARIA O BREAK:
    ## EXEMPLO:

for numero in range(100):
    if numero % 2 == 0:
            continue

    print(numero, end =" ")
