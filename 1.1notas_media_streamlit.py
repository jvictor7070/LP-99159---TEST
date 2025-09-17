import streamlit as st

st.title("Laços de Repetição")

st.write("Escreva um algoritmo que solicite duas notas para")

nota1 = st.number_input("digite a primeira nota: ", min_value=0, max_value=10)
nota2 = st.number_input("digite a segunda nota: ", min_value=0, max_value=10)

soma = nota1 + nota2
media = soma / 2

if st.button("calcular média"):
    st.info(f"Média: {media}")