import os
os.system("cls")

notas = 0

for i in range(3):
    while True:
        try:
            nota = float(input(f"Digite a nota {i + 1}: "))

            if 0 <= nota <= 10:
                notas.append(nota)
            else:
                print("Nota inválida! Digite um valor entre 0 e 10.")
        except ValueError:
            print("Entrada inválida! Por favor, digite um número.")

media = sum(notas) / len(notas)

# Imprime a média
print(f"\nA média das notas é: {media:.2f}")

if media >= 7:
    print("O aluno está APROVADO.")
elif 5 <= media < 7:
    print("O aluno está em RECUPERAÇÃO.")
else:
    print("O aluno está REPROVADO.")