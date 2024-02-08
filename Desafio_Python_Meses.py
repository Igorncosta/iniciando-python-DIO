#definindo a variável month
month = int(input())

# Dicionário com os meses em inglês
months_dict = {
    1: "January",
    2: "February",
    3: "March",
    4: "April",
    5: "May",
    6: "June",
    7: "July",
    8: "August",
    9: "September",
    10: "October",
    11: "November",
    12: "December"
}

# Verificando se o mês está dentro do intervalo permitido
if 1 <= month <= 12:
    print(months_dict[month])