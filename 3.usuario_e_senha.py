import os
os.system("cls")

tentativas = 0
login_salvo = "soco"
senha_salva = "7070"

# O loop while continua enquanto 'tentativas' for menor que 3
while tentativas < 3:
    print(f"\nTentativa: {tentativas + 1}")
    login = input("Digite seu usuário: ")
    senha = input("Digite sua senha: ")

    # Verifica se as credenciais estão corretas
    if login == login_salvo and senha == senha_salva:
        print("Seja Bem-Vindo!")
        # Se as credenciais estiverem corretas, sai do loop
        break
    else:
        print("Login ou senha inválidos.")
        # Se as credenciais estiverem erradas, aumenta a contagem de tentativas
        tentativas += 1

# Depois que o loop while termina, verifica se o usuário esgotou as tentativas
if tentativas == 3:
    print("\nVocê excedeu o número máximo de tentativas. Acesso bloqueado.")