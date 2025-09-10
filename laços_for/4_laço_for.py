#verifique as idades de uma pessoa 
#se menor que 18, mostre:menor de idade.
#caso contrario,mostre:maior de idade.
#usando streamlit.

import streamlit as st

st.title("verificando a idade")

idade=st.number_input("digite sua idade:",min_value=0, max_value=130,step=1)

if st.button("verificar"):
    if idade <18:
        st.write("menor de idade.")
    else:
        st.write("maior de idade.") 


else: 
    st.warning("por favor,digite a idade.")