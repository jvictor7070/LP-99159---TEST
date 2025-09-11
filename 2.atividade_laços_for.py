import streamlit as st
import time

st.title("atividade 1")

st.header("Laços de repetição: For:")
st.write("escreva números ímpares entre 1 e 20.")

if st.button("iniciar"):
    for i in range(1,21,2):
        st.info(i)
        time.sleep(2)
    st.header("Fim")    