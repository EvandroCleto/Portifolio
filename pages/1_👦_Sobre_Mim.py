import streamlit as st
import streamlit.components.v1 as components
from PIL import Image

st.set_page_config(
    page_title="Sobre Mim",
    page_icon="👦",
)

col1, col2 = st.columns(2)

with col1:
    st.markdown('<div style="font-size: 14px">Olá. Eu sou o Evandro Cleto, Data Scientist Certified Specialist, certificado pela Data Science Academy, pai do Gabriel, corredor amador e aspirante a cozinheiro (o Gabriel fala que o melhor arroz e feijão do mundo é o do papai!!</div>', unsafe_allow_html=True)
    st.markdown('<div style="font-size: 14px">Com três anos de dedicação na aplicação de IA, Ciência de Dados e Machine Learning para desvendar enigmas empresariais, eu sou tipo o Sherlock Holmes da tecnologia!</div>', unsafe_allow_html=True)
    st.markdown('<div style="font-size: 14px">Também sou um veterano da reserva com 14+ anos de batalhas heroicas, onde salvei empresas com as ferramentas do ERP Totvs Protheus!</div>', unsafe_allow_html=True)
    #st.markdown('<div style="font-size: 14px">Sou fluente em SQL, o que significa que posso falar a língua das bases de dados como ninguém!</div>', unsafe_allow_html=True)
    st.markdown('<div style="font-size: 14px">E não parei por aqui. No momento estou me atualizando e desenvolvendo projetos que usam ferramentas como Transformer, LLMs, Langchain, Vector Databases e Hugging Face que são o estado da arte em IA Generativa.</div>', unsafe_allow_html=True)
    st.markdown('<div style="font-size: 14px">É um prazer receber sua visita.</div>', unsafe_allow_html=True)
    st.text("")
    #st.markdown('<div style="font-size: 14px">Ah, se você estiver com pressa, o meu currículo está aqui:</div>', unsafe_allow_html=True)
    #st.text("")
    #pdfFileObj = open("/mount/src/portifolio/Curriculo_DS_PT_V1.pdf", 'rb')
    #pdfFileObj = open("Curriculo_DS_PT_V1.pdf", 'rb')
    #st.download_button('Baixe meu CV:',pdfFileObj,file_name='Curriculo_Evandro_Cleto.pdf',mime='pdf')

with col2:
    image = Image.open('Main_Photor.jpg')
    st.image(image,width=280,caption='2016 Ultimate XC-60Km - 10º Lugar Geral')

    
