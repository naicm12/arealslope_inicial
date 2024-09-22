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
    st.write("📍 Local da largada: Rua Alexandre Guimarães com José de Alencar - s/n, Bairro Areal")
    st.caption("")
    st.write("💲 Valor da Inscrição: 90,00 reais para 7km; 100,00 para 14km e 115,00 para 21km")
    st.write("Forma de Pagamento: ")
    st.write("  Pix kelioesteves@hotmail.com - Kélio Esteves Xavier - Mercado pago.")
    st.write("📱 Mais informações: (69) 99925-9005")
    st.caption("")
    st.write("🏆 Havará premiação de troféus e valor líquido aos atletas classificados do 1º ao 5º lugar para o percurso de 21km masculino e feminino geral, conforme segue abaixo:")
    st.write("  1° LUGAR R$ 600,00")
    st.write("  2° LUGAR R$ 400,00")
    st.write("  3° LUGAR R$ 300,00")
    st.write("  4° LUGAR R$ 200,00")
    st.write("  5° LUGAR R$ 150,00")
    st.write(" Nas demais categorias por faixa etária do percurso de 21km haverá premiação somente de troféus do 1º ao 3º colocados")
    st.write(" No percurso de 14km haverá premiação de troféus do 1º ao 5º colocados nas categorias geral masculino e feminino e do 1º ao 3º colocados nas categorias por falxa etárias masculino e feminino.")        
    st.write(" No percurso de 7km haverá premiação de trofeus do 1º ao 5º colocados apenaas pra categoria geral masculino e feminino.")
    st.write("O Kit do atleta será composto por camiseta, número de peito, água, frutas e medalha, sendo os três últimos itens a serem retirados no dia da corrida")
    st.caption("")
    st.write("INSCRIÇÕES:")
    st.write("✍️ Período de inscrição:")
    st.write("  Início: 22 de setembro de 2024")
    st.write("  Término: 30 de novembro de 2024 ou até o limite das vagas")
    st.write("A entrega dos kits será realizada do dia 14/01/2025, no seguinte endereço: Rua José de Alencar esquina com Alexandre Guimarães, s/n - Areal, horário: 10:00 às 19:00h")
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
