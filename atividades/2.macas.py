import os
os.system("cls")

macas = int(input("Quantidade de maçãs:"))

preco = macas * 1.30
desconto = macas * 1

if macas <= 11:
    print(f"As maçãs custarão:R${preco}")
else:
    print(f"As maçãs custarão:R${desconto}")    



