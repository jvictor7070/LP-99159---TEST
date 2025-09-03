
import os
os.system("cls")

n1 = int(input("digite um número:"))      
n2 = int(input("digite um número:"))    
opr =input("digite sua operação básica(+, -, *, /):") 
resultado = int

match opr:
    case "+":
        resultado = n1 + n2
    case "-":
        resultado = n1 - n2
    case "*":
        resultado = n1 * n2
    case "/":
        resultado = n1 / n2
    case _:
        resultado = "operação inválida"

print(f"primeiro número: {n1}")   
print(f"segundo número: {n2}")   
print(f"operação escolhida: {opr}")   
print(f"resultado: {resultado}")   





