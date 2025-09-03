

nota_1 = int(input("digite a primeira nota: "))
nota_2 = int(input("digite a segunda nota: "))
nota_3 = int(input("digite a terceira nota: "))

soma = nota_1 + nota_2 + nota_3
media = soma / 3



print(f"média: {media}")

if media >= 7:
    print("você foi aprovado")
else:
    print("você foi reprovado") 


