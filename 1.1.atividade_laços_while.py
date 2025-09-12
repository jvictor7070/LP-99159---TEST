import os
os.system("cls")

print("Laços de Repetiçao - while")

while True:
    nota = float(input("digite sua nota: "))
    if nota <0 or nota>10:
        nota = float(input("digite sua nota: "))
    else: 
        break
print(f"sua nota é: {nota}")
    
