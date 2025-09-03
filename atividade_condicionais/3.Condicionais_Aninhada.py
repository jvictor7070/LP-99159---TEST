#Condicional Aninhada

import os
os.system("cls")

idade = float (input("digite sua idade: "))

if idade >=18:
    print("Maior de idade: ")
elif idade >= 14:
    print("Adolescente")
else:
    print("Criança ")    

    print("fim.")