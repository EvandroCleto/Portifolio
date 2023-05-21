import streamlit as st
import streamlit.components.v1 as components
from PIL import Image

st.set_page_config(
    page_title="Sobre Mim",
    page_icon="👦",
)

col1, col2 = st.columns(2)

with col1:
    st.markdown("Olá. Eu sou o Evandro Cleto, Data Scientist (Formado e Certificado pela Data Science Academy), Consultor ERP Totvs Protheus, pai do Gabriel, Ultra-maratonista amador e aspirante a cozinheiro(O Gabriel fala que o melhor arroz e feijão do mundo é o do Papai!!)")
    st.markdown("Tenho 14+ anos de experiência em solucionar problemas de negócio utilizando como ferramentas, o ERP Totvs Protheus nas áreas de Faturamento, Produção, Estoque, Financeiro, Gestão de Contratos e de Serviços, SQL e mais recentemente, Machine Learning.")
    st.markdown("É um prazer receber sua visita e compartilhar um pouco da minha experiência com você.")

with col2:
    image = Image.open('Main_Photor.jpg')
    st.image(image,width=240,caption='Ultimate XC-60Km')

col3, col4 = st.columns(2)

with col3:
    image = Image.open('Badge_FCD.png')
    st.image(image,width=140)

with col4:
    image = Image.open('Badge DSCP.png')
    st.image(image,width=160)
    
