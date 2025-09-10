import streamlit as st

st.title("verificando média")

media = st.number_input("digite a media: ")

if st.button ("verificar: "):
    if media >= 7:
        st.success("aprovado")
    else: st.warning("reprovado")
else:
    st.info("informe a media")

# success - verde
# warning - amarelo
# info - azul
# error - vermelho
