
import os
os.system("cls")

login = input("login: ")
senha = int(input("senha: "))
usuario = "futurodosenai@gmail.com"
s= int(7070)

if login == usuario and senha == s:
    print("bem-vindo!")
else:
    print("login ou senha inválidos")


