# algoritmo que solicite ao usuário 5 valores inteiros e, no final, informe quantos desses números são pares e quantos são ímpares.

import streamlit as st
import time

st.title("Atividade 6: Contador de Pares e Ìmpares")
st.write("Escreva um algoritmo que solicite ao usuário 5 valores inteiros e, no final, informe quantos desses números são pares e quantos são ímpares.")

pares = 0
impares = 0
for i in range(1,6):
    numero = st.number_input(f"digite o {i}º número: ", step=1)
    if numero % 2 == 0:
        pares = pares + 1
    else:
        impares = impares + 1


if st.button("Verificar"):
    st.info(f"Quantidade de Pares: {pares}")
    st.info(f"Quantidade de Impares: {impares}")

st.header("Fim")
st.snow()    