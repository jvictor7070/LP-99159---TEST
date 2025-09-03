
import os
os.system("cls")

dia = int(input("digite um número para o dia da semana: "))

match dia:
    case 1:
        print("domingo")
    case 2:
        print("segunda")
    case 3:
        print("terça")
    case 4:
        print("quarta")
    case 5:
        print("quinta")
    case 6:
        print("sexta")
    case 7:
        print("sábado")
    case _:
        print("opção inválida") 

print('fim')   
                                
