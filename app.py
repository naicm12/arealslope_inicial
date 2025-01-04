import streamlit as st
from datetime import date

#st.markdown("### 🔒Inscrições Encerradas")
from PIL import Image
img = Image.open('02.jpg')
st.image(img)
st.markdown("### 1ª Corrida Areal Slope")
st.write("")
st.markdown("### 🔒Inscrições Encerradas")
#st.link_button(label="Clique aqui para realizar sua inscrição",url="https://arealslope-inscricao-050956b44d4a.herokuapp.com/",type="primary")

with st.form("Informativo", border=False):
    st.markdown("##### Informativo da Corrida")
    with open('Informativo.txt', 'r', encoding='UTF-8') as f:
        lines = f.readlines()
        for line in lines:
            st.write(line)

    st.warning("ATENÇÃO",icon="⚠️")
    st.warning("  No dia da retirada do kit ou no dia da prova, o atleta deverá levar 1 Kg de alimento não perecível (menos sal e açúcar)")
    st.form_submit_button("",disabled=True)

with st.form("Regulamento"):
    st.markdown("##### Regulamento")
    with open('Regulamento.txt', 'r', encoding='UTF-8') as f:
        lines = f.readlines()
        for line in lines:
            st.write(line)
    #st.link_button(label="Clique aqui para realizar sua inscrição",url="https://arealslope-inscricao-050956b44d4a.herokuapp.com/",type="primary")
    st.form_submit_button("",disabled=True)

from PIL import Image
img = Image.open('003.png')
st.image(img)
