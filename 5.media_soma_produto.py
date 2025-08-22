


valor_1 =int(input("digite o primeiro valor: ")) 
valor_2 = int(input("digite o degundo valor: "))  

soma = valor_1 + valor_2
produto = valor_1 * valor_2

if valor_1 > valor_2:
    maior = valor_1
    menor = valor_2
else:
    maior = valor_2
    menor = valor_1

    maior = max(valor_1, valor_2)
    menor = min(valor_1, valor_2)

    print(f"soma: {soma}")
    print(f"produto: {produto}")
    print(f"maior número: {maior}")
    print(f"menor número: {menor}")
