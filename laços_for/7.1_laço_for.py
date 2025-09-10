import streamlit as st
import time

st.title("Laços de repetição - for")
st.header("Contagem 1 a 10")

numero = st.number_input("digite até onde quer o laço de repetição:", step=1)

if st.button("Iniciar"):
    for i in range(2,numero + 1,2):
        st.write(i)
        time.sleep(1)
    st.header("Fim")