import streamlit as st
from datetime import date

#st.markdown("### 🔒Inscrições Encerradas")
from PIL import Image
img = Image.open('02.png')
st.image(img)
st.markdown("### 1ª Corrida Areal Slope")
st.write("")
#st.markdown("### 🔒Inscrições Encerradas")

st.link_button(label="Clique aqui para realizar sua inscrição",url="https://arealslope-inscricao-050956b44d4a.herokuapp.com/",type="primary")

with st.form("Informativo", border=False):
    st.markdown("##### Informativo da Corrida")
    st.write("📅 Dia 19 de janeiro de 2025")
    st.write("🏃🏻 Largada às 06hs 🕗")
    #st.write("📍 Saída: Início do Espaço Alternativo - Av. Jorge Teixeira (Praia)")
    st.caption("")
    st.write("💲 Valor da Inscrição: 90,00 reais para 7km; 100,00 para 14km e 115,00 para 21km")
    st.write("Forma de Pagamento: ")
    st.write("  Pix kelioesteves@hotmail.com - Kélio Esteves Xavier - Mercado pago.")
    st.write("📱 Mais informações: (69) 99925-9005/ (69) 99308-8323 / (69) 99958-3207")
    st.caption("")
    st.write("🏆 Havará premiação aos atletas classificados do 1º ao 5º lugar para o percurso de 21km masculino e feminino geral, conforme segue abaixo:")
    st.write("  1° LUGAR R$ 600,00")
    st.write("  2° LUGAR R$ 400,00")
    st.write("  3° LUGAR R$ 300,00")
    st.write("  4° LUGAR R$ 200,00")
    st.write("  5° LUGAR R$ 150,00")
    st.write("O Kit do atleta será composto por camiseta, número de peito, água, frutas e medalha, sendo os três últimos itens a serem retirados no dia da corrida")
    st.caption("")
    st.write("INSCRIÇÕES:")
    st.write("✍️ Período de inscrição:")
    st.write("  Início: 23 de setembro de 2024")
    st.write("  Término: 19 de janeiro 2025 ou até o limite das vagas")
    st.warning("ATENÇÃO",icon="⚠️")
    st.warning("  No dia da retirada do kit ou no dia da prova, o atleta deverá levar 1 Kg de alimento não perecível (menos sal e açúcar)")
    st.form_submit_button("",disabled=True)

with st.form("Regulamento"):
    st.markdown("##### Regulamento")
    with open('Regulamento.txt', 'r', encoding='UTF-8') as f:
        lines = f.readlines()
        for line in lines:
            st.write(line)
    st.link_button(label="Clique aqui para realizar sua inscrição",url="https://arealslope-inscricao-050956b44d4a.herokuapp.com/",type="primary")
    #st.link_button(label="Clique aqui para realizar sua inscrição",url="http://191.217.246.233:8501/",type="primary")
    st.form_submit_button("",disabled=True)

from PIL import Image
img = Image.open('003.png')
st.image(img)