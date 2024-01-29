def sacar(valor): # O 'DOIS PONTOS' DECLARA O INICIO DE UMA IDENTAÇÃO. OU SEJA, A PRÓXIMA LINHA DEVERÁ CONTER 4 ESPAÇOS.
    saldo = 1000
    print("Saldo", saldo)
    if saldo >=valor:
        print("O valor de", valor, "foi retirado com êxito!")
        print("Retire-o agora!")
        
    print("Obrigado pela preferência!")
### tudo que esta aqui dentro corresponde somente a este método "sacar". Ou seja, só vai
    ### fazer efeito dentro deste espaço. Para eu chamar "saldo" novamente eu tenho que 
    ### definir um valor a ele, que eu não aprendi ainda.

sacar(100)

def depositar(valor):
    saldo = 1000
    saldo +=valor
    print("Obrigado pela preferência!")
    print("O Valor de:", valor, "foi depositado!")


depositar(1000)