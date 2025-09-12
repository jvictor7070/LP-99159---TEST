import streamlit as st

st.title("Laço de repetição - While")

QUANTIDADE_DE_NOTAS = 2
soma = 0

for i in range(QUANTIDADE_DE_NOTAS):
    while True:
         nota = st.number_input(f"digite sua {i + 1}ª nota:")
         if nota <0 or nota>10:
            nota = float(input("digite sua nota: "))
         else: 
                break
    soma = soma + nota

media = soma / QUANTIDADE_DE_NOTAS

st.info(f"Média: {media}")
    