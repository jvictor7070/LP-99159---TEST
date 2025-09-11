import streamlit as st
import time

st.title("Contagem Regressiva")

st.header("Laços de repetição: For:")
st.write("escreva um algoritmo que solicite ao usúario um número e faça a contagem regressiva.")

numero = st.number_input("informe um número", step = 1)

if st.button("start"):
    for i in range(numero,0,-1):
        st.info(i)
        time.sleep(1)
    st.header("Fim") 
    st.balloons()
    st.snow() 
else:
    st.info("informe o número") 

 