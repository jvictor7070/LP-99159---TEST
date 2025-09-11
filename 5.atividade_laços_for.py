import streamlit as st
import time

st.title("Soma de 5 números inteiros")

st.header("Laços de repetição: For:")
st.write("escreva um algoritmo que solicite ao usúario um número e faça a contagem regressiva.")

soma = 0
for i in range(1,6):
    numero = st.number_input(f"digite o {i} número:", step = 1, min_value=0)
    soma = soma + numero
    time.sleep(1)

if st.button("iniciar"):
    st.success(f"a soma dos números é: {soma}")
else:
    st.info("Informe um número")    