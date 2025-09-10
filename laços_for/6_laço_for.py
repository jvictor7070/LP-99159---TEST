import streamlit as st

st.title("média, soma, produto")


n1 = st.number_input("digite o primeiro número: ")
n2 = st.number_input("digite o segundo número: ")

media = (n1 + n2) / 2
produto  = n1 * n2
soma = n1 + n2
menor = min(n1, n2)
maior = max(n1, n2)

if st.button("calcular:"):
    if n1 and n2:
        st.write(f"média:{media}") 
        st.write(f"soma:{soma}")
        st.write(f"produto:{produto}")
        st.write(f"menor:{menor}")
        st.write(f"maior:{maior}")
else:
    st.info("Informe os números.")    



# success -  verde
# warning - amarelo
# info - azul
# error - vermelho
