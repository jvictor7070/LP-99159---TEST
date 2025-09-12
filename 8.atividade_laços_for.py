
# Calcula a média de 3 notas e determina o status de aprovação de um aluno (Aprovado, Recuperação ou Reprovado)

import streamlit as st

st.title("Atividade 8: Laços de Repetição_For")
st.header(" Calcula a média de 3 notas e determina o status de aprovação de um aluno (Aprovado, Recuperação ou Reprovado)")

soma = 0

for i in range(3):
    nota = st.number_input(f"digite sua {i + 1}ª nota:")
    soma = soma + nota

media = soma / 3

if st.button("Verificar Média"):
    st.info(f"Média: {media}")
    if media <=10 >= 7:
        st.success("Parabéns,você foi aprovado")
    elif media <= 4:
        st.error("Infelizmente,você foi reprovado")
    else :
        st.warning("você foi para recuperação")
else:
    st.info("Informe sua nota.")        

