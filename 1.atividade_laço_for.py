# escreva um algoritmo que mostre os números pares entre 100 e 120

import streamlit as st
import time

st.title("atividade 1")

st.header("Laços de repetição: For:")

if st.button("iniciar"):
    for i in range(100,121,2):
        st.info(i)
        time.sleep(2)