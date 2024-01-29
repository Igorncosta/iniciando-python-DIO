opcao = -1

while opcao != 0:
    opcao = int(input("Escolha: \n [1] SAQUE \n [2] EXTRATO \n [0] SAIR \n: "))

    if opcao == 1:
        print("Sacando:")

    elif opcao == 2:
        print("Exibindo extrato ...")
else: 
    print("Obrigado por escolher a gente!")

## ENQUANTO O "IF" TESTA E EXECUTA APENAS UMA VEZ. O "WHILE" VAI EXECUTAR TODA VEZ QUE FOR ATENDIDA.
        ## OU SEJA, QUANDO FOR ATENDIDA O PROGRAMA FINALIZA.