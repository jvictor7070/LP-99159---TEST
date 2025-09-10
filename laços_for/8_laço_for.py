import streamlit as st
import time

st.title("Laços de repetição - for")
st.header("Contagem 1 a 10")


if st.button("Iniciar"):
    for i in range(100,+2,121):
        st.write(i)
        time.sleep(1)
    st.header("Fim")