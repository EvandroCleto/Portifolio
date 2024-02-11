import streamlit as st
import streamlit.components.v1 as components
from PIL import Image

st.set_page_config(
    page_title="Sobre Mim",
    page_icon="👦",
)

col1, col2 = st.columns(2)

with col1:
    st.markdown('<div style="font-size: 14px">Olá. Eu sou o Evandro Cleto, Data Scientist Certified Specialist, formado e certificado pela Data Science Academy, pai do Gabriel, ultra-maratonista amador e aspirante a cozinheiro (o Gabriel fala que o melhor arroz e feijão do mundo é o do papai!!</div>', unsafe_allow_html=True)
    st.markdown('<div style="font-size: 14px">Com três anos de dedicação na aplicação de Inteligência Artificial, Ciência de Dados e Machine Learning para desvendar enigmas empresariais, eu sou tipo o Sherlock Holmes da tecnologia!</div>', unsafe_allow_html=True)
    st.markdown('<div style="font-size: 14px">E como se não bastasse, também sou um veterano com 14+ anos de batalhas heroicas, salvando empresas com as ferramentas do ERP Totvs Protheus em áreas como Faturamento, Produção, Estoque, Financeiro, Gestão de Contratos e de Serviços!</div>', unsafe_allow_html=True)
    st.markdown('<div style="font-size: 14px">E não se preocupe, meu amigo, sou fluente em SQL, o que significa que posso falar a língua das bases de dados como ninguém!</div>', unsafe_allow_html=True)
    st.markdown('<div style="font-size: 14px">É um prazer receber sua visita e compartilhar um pouco da minha experiência com você.</div>', unsafe_allow_html=True)

with col2:
    image = Image.open('Main_Photor.jpg')
    st.image(image,width=240,caption='Ultimate XC-60Km')

    
