import streamlit as st

def mostrar_tabuada_streamlit():

    st.title("Gerador de Tabuada")
    st.write("Digite um número e a tabuada de multiplicação será exibida abaixo.")
    
    numero = st.number_input("Digite um número:", min_value=0, step=1)

    # Verifica se o usuário digitou um número
    if numero is not None:
        st.subheader(f"Tabuada do número {int(numero)}:")

        # Loop de 1 a 10 para calcular e exibir a tabuada
        for i in range(1, 11):
            resultado = numero * i
            st.write(f"{int(numero)} x {i} = {int(resultado)}")

# Chama a função para executar a aplicação Streamlit
if __name__ == "__main__":
    mostrar_tabuada_streamlit()