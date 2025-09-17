import streamlit as st

st.title("Laços de Repetição_While")

st.write("crie um programa que solicite ao usuário seu login e uma senha, o programa deve continuar pedindo o login e a senha ate que ambos estejam corretos")

login_salvo = "soco"
senha_salva = "7070"

login = st.text_input("digite seu login: ")
senha = st.text_input("digite sua senha: ", type="password")

if st.button("verificar"):
    if login == login_salvo and senha == senha_salva:
        st.success("Seja Bem-Vindo!")
    else:
        st.warning("Login ou senha inválidos. ")    


