import os
os.system("cls")

valor_produto = float(input("Informe o valor do produto: "))

# Solicita a forma de pagamento
print("Escolha a forma de pagamento:")
print("1 - Pagamento à vista")
print("2 - Pagamento a prazo")
forma_pagamento = input("Digite 1 ou 2: ")

# Utiliza a estrutura match-case para decidir a lógica
match forma_pagamento:
    case '1':
        # Lógica para pagamento à vista
        valor_desconto = valor_produto * 0.10
        total_a_pagar = valor_produto - valor_desconto
        
        print("\n--- Recibo de Pagamento à Vista ---")
        print(f"Valor do produto: R$ {valor_produto:.2f}")
        print("Forma de pagamento: À vista")
        print(f"Valor do desconto: R$ {valor_desconto:.2f}")
        print(f"Total a pagar: R$ {total_a_pagar:.2f}")
    
    case '2':
        # Lógica para pagamento a prazo
        while True:
            try:
                quantidade_parcelas = int(input("Informe a quantidade de parcelas (até 6): "))
                if 1 <= quantidade_parcelas <= 6:
                    break
                else:
                    print("Número de parcelas inválido. Digite um valor entre 1 e 6.")
            except ValueError:
                print("Entrada inválida. Por favor, digite um número.")
        
        valor_parcela = valor_produto / quantidade_parcelas
        
        print("\n--- Recibo de Pagamento a Prazo ---")
        print(f"Valor do produto: R$ {valor_produto:.2f}")
        print("Forma de pagamento: A prazo")
        print(f"Quantidade de parcelas: {quantidade_parcelas}")
        print(f"Valor por parcela: R$ {valor_parcela:.2f}")
        print(f"Total a prazo: R$ {valor_produto:.2f}")
    
    case _:
        # Caso a entrada seja inválida (funciona como o 'else')
        print("Opção de pagamento inválida. Por favor, execute o programa novamente e digite 1 ou 2.")