import os
os.system("cls") 

nome = input("digite seu nome: ")
nota1 = float(input("digite sua nota: "))
nota2 = float(input("digite sua nota: "))
soma = nota1 + nota2
media = soma / 2

a = "nota A"
b = "nota B"
c = "nota C"
d = "nota D"
e = "nota E"

print(f"sua nota é: {media}")

if media >= 9:
    print(f"aprovado, {a}")
elif media >= 7.5:
    print(f"aprovado, {b}")
elif media >= 6:
    print(f"aprovado, {c}")
elif media >= 4:
    print(f"reprovado, {d}")
else:
    print(f"reprovado, {e}")



