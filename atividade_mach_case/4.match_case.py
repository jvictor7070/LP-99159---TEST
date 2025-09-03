import os
os.system("cls")

mes = int(input("digite o número referente ao mês: "))

match mes:
    case 1:
        print("JANEIRO")
    case 2:
        print("fEVEREIRO")
    case 3:
        print("MARÇO")
    case 4:
        print("ABRIL")
    case 5:
        print("MAIO")
    case 6:
        print("JUNHO")
    case 7:
        print("JULHO")
    case 8:
        print("AGOSTO")
    case 9:
        print("SETEMBRO")
    case 10:
        print("OUTUBRO")
    case 11:
        print("NOVEMBRO")
    case 12:
        print("DEZEMBRO")
    case _:
        print("NÚMERO INVÁLIDO")