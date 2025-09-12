import streamlit as st

st.title("Atividade 7: Laços de Repetição_For")
st.header("calcula a média de 4 notas")
soma = 0

for i in range(4):
    nota = st.number_input(f"digite sua {i+1}ª nota:")
    soma = nota + soma

media = soma / 4

if st.button("Resultado"):
    st.info(f"média: {media}")

