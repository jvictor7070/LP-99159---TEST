import os
os.system("cls")

QUANTIDADE_DE_NOTAS = 2
soma = 0

for i in range(QUANTIDADE_DE_NOTAS):
    while True:
        nota = float(input("digite sua nota: "))
        if nota< 0 or nota > 10:
            print("a nota inválida")
        else:
            soma += nota
            break

media = soma / QUANTIDADE_DE_NOTAS

print(f"Média: {media}")