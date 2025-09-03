import os
os.system ("cls")

n1 = int (input ('digite o primeiro valor : '))
n2 = int (input ('digite o segundo valor : '))

# Realizando cálculos (PROCESSAMENTO)
soma = n1 + n2
media = soma / 2
produto = n1 * n2
menor_valor = min(n1, n2) 
maior_valor = max(n1, n2) 

# Exibindo dados(saída)
print(f'sua soma é:{soma}')
print(f'sua média é:{media}')
print(f'os valores são iguais:{produto}')

if n1 == n2:
    print(f'o menor valor é:{menor_valor}')
else:
    print(f'o menor valor é:{menor_valor}')
    print(f'o maior valor é:{maior_valor}')