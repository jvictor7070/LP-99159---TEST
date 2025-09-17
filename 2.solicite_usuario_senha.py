import os
os.system("cls")


print("Laços de Repetição_While")
print("""
Crie um programa que solicite ao usuário seu login e uma senha.""")
print("O programa deve continuar pedindo o login e a senha ate que ambos estejam corretos.")

login_salvo = "soco"
senha_salva = 7070

while True:
    login = input("""
loginDigite seu usuário: """)
    senha = input("Digite sua senha: ")

    if login == login_salvo and senha == senha_salva:
        print("Seja Bem-Vindo!")
        break
    else:
        print("Login ou senha inválidos")