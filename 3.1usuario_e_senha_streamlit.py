import streamlit as st
 
st.title("Laços de Repetição_While")
st.write("usuario e senha com limite de 3 tentativas")

login_salvo = "soco"
senha_salva = "7070"

st.session_state.setdefault("desabilitar", False)
st.session_state.setdefault("tentativas", 0)

login = st.text_input("digite seu login: ", disabled=st.session_state.desabilitar)
senha = st.text_input("digite sua senha: ", type="password", disabled=st.session_state.desabilitar)

if st.button("verificar"):
    if login == login_salvo and senha == senha_salva:
        st.success("Bem_vindo")
    else:
        st.session_state.tentativas +=1
        if st.session_state.tentativas <=3:
            st.warning(f"Login ou senha inválidos, tentativas: {st.session_state.tentativas}")
        else:
            st.session_state.desabilitar = True    
            st.error("Número de tentativas inválidas") 
