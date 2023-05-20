import streamlit as st
import streamlit.components.v1 as components
from PIL import Image

st.set_page_config(
    page_title="Projetos Acadêmicos em Data Science",
    page_icon="🧱",
)

with st.container():
    
    col1, col2, col3 = st.columns(3)

    with col1:
        
        st.markdown("" )

    with col2:
       
        image = Image.open('Logo_DSA.png')
        st.image(image,width=250)
    
    with col3:
        
        st.markdown("" )

st.markdown("## Projetos Acadêmicos em Data Science")

st.markdown("Aqui estão alguns dos projetos de Data Science que estudei ao longo da Formação Cientista de Dados na Data Science Academy(https://www.datascienceacademy.com.br/bundle/formacao-cientista-de-dados).")

with st.container():

    st.markdown("----------------")    
    
    col4, col5 = st.columns(2)

    with col4:
        
        st.markdown("### Análise de Séries Temporais no Mercado Financeiro.")   


    with col5:
       
        image = Image.open('D:\Portifolio\Page_4-Projetos_Academicos\fontes\Ser_Temp_R.png')
        st.image(image,width=350)

    
    col6 = st.columns(1)
    
    st.markdown("**Resumo:** ")
    st.markdown(" Projeto de séries temporais em linguagem R para analisar dados do mercado financeiro.")
    #st.markdown("**Acesse o fonte do projeto aqui:** https://github.com/EvandroCleto/Machine-Learning-em-Logistica-Prevendo-o-Consumo-de-Energia-de-Carros-Eletricos/blob/main/Projeto01V3_0-Consumo_Carros_Eletricos.R")