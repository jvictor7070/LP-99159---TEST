import streamlit as st
import time

st.title("Gerador de Tabuada")
st.write("Digite um número e a tabuada de multiplicação será exibida abaixo.")
    
numero = int(st.number_input("Digite um número:", step = 1))

if st.button("iniciar"):
    for i in range(1,21,1):
        resultado = numero * i
        st.info(f"{int(numero)} x {i} = {int(resultado)}")
        time.sleep(2)
    st.header("Fim")    