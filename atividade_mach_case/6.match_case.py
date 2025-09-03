import os
os.system("cls")




altura = float(input("digite sua altura:"))
print("""
    digite M para masculino
    ou  F para feminino     
      """)
sexo = input("digite seu sexo: ")

match sexo:
    case "m":
        peso_ideal = (72.7 * altura) - 58
        print(f"sua altura: {altura}")
        print("sexo: Masculino")
        print(f"peso ideal: {peso_ideal}")
    case "f":
        peso_ideal = (62.1 * altura) - 44.7
        print(f"sua altura: {altura}")
        print("sexo: Feminino")
        print(f"peso ideal: {peso_ideal}")

       
















