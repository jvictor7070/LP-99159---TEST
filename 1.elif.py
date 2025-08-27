#elif

import os
os.system("cls")

idade = int(input("digite sua idade: "))

if idade <= 15:
    print("não pode votar")
elif idade <= 17: 
    print("voto opcional")
elif idade <= 65:
    print("voto obrigatório")
else:
    print("não é obrigatório votar")        