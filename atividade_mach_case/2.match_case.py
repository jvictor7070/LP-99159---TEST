import os
os.system("cls")

print("""
código \t prato \t\t valor
 1 \t Picanha \t R$25,00  
 2 \t Lasanha \t R$20,00  
 3 \t Strogonoff \t R$18,00  
 4 \t Bife Acebolado\t R$15,00  
 5 \t Pão com Ovo \t R$5,00                       

""")

codigo = int(input("digite o código do prato desejado: "))

match codigo:
    case 1:
        print("pedido: picanha  \ valor: R$25,00 reais ")
    case 2:
        print("pedido: Lasanha  \ valor: R$20,00 reais ")
    case 3:
        print("pedido: Strogonoff  \ valor: R$18,00 reais ")
    case 4:
        print("pedido: Bife Acebolado  \ valor: R$15,00 reais ")
    case 5:
        print("pedido: Pão com Ovo  \ valor: R$5,00 reais ")
    case _:
        print("Pedido não se encontra no cárdapio ")