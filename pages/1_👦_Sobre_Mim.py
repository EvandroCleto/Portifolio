import streamlit as st
import streamlit.components.v1 as components
from PIL import Image

st.set_page_config(
    page_title="Sobre Mim",
    page_icon="👦",
)

col1, col2 = st.columns(2)

with col1:
    st.markdown("**Olá. Eu sou o Evandro Cleto, Data Scientist (Formado e Certificado pela Data Science Academy), Consultor ERP Totvs Protheus, pai do Gabriel, Ultra-maratonista amador e aspirante a cozinheiro(O Gabriel fala que o melhor arroz e feijão do mundo é o do Papai!!)**")
    st.write("")
    st.markdown("**É um prazer ter a sua visita e poder compartilhar um pouco da minha experiência com você.**")

with col2:
    image = Image.open('Main_Photor.jpg')
    st.image(image,width=150,caption='Ultimate XC-60Km')

col3, col4 = st.columns(2)

with col3:
    image = Image.open('Badge_FCD.png')
    st.image(image,width=140)

with col4:
    image = Image.open('Badge DSCP.png')
    st.image(image,width=160)
    
