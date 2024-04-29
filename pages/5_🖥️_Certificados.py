import streamlit as st
import streamlit.components.v1 as components
import numpy as np
from PIL import Image

st.set_page_config(
    page_title="Certificados",
    page_icon="🖥️",
)

st.markdown("### Com muito orgulho apresento meus certificados obtidos através da minha minha jornada como Cientista de Dados.") 

st.markdown("----------------")   
st.markdown("**Certificação DSCS(Data Scientist Certified Specialist)**")
image1 = Image.open('DSCS_CERT.png')
st.image(image1,width=500)

st.markdown("----------------")   
st.markdown("**Certificação DSCP(Data Scientist Certified Professional)**")
image1 = Image.open('DSCP_CERT.png')
st.image(image1,width=500)

st.markdown("----------------")   
st.markdown("**Prompt Engineering com ChatGPT Para Análise de Dados e Data Science**")
image1 = Image.open('Cert_Prompt.jpg')
st.image(image1,width=500)

st.markdown("----------------")   
st.markdown("**Formação Engenheiro de Inteligência Artificial 3.0...**")
#image1 = Image.open('Cert_FCD.png')
#st.image(image1,width=500)

st.markdown("**... que é composta pelos cursos:**")

col14, col15  = st.columns(2)
width=230
with col14:
    st.markdown(">**1. Deep Learning for AI Applications with PyTorch and Lightning**")
    image1 = Image.open('Cert_DL_Pytorch.jpg')
    st.image(image1,width=width)
with col15:
    st.markdown(">**2. Natural Language Processing with Transformers e LLMs**")
    image1 = Image.open('Cert_PNL_Transformers.jpg')
    st.image(image1,width=width)

st.markdown("----------------")   
st.markdown("**Formação Inteligência Artificial...**")
image1 = Image.open('Cert_FIA.jpg')
st.image(image1,width=500)

st.markdown("**... que é composta pelos cursos:**")

col7, col8, col9  = st.columns(3)
width=230
with col7:
    st.markdown(">**1. Introdução à Inteligência Artificial**")
    image1 = Image.open('Cert_Into_IA.png')
    st.image(image1,width=width)
with col8:
    st.markdown(">**2. Deep Learning Frameworks**")
    st.text("")
    image1 = Image.open('Cert_DeepL_Frame.png')
    st.image(image1,width=width)
    
with col9:
    st.markdown(">**3. Programação Paralela em GPU**")
    image1 = Image.open('Cert_Prog_Paralela.png')
    st.image(image1,width=width)
    
col10, col11, col12  = st.columns(3)
width=230
with col10:
    st.markdown(">**4. Deep Learning I**")
    st.text("")
    image1 = Image.open('Deep_LearningI.png')
    st.image(image1,width=width)
with col11:
    st.markdown(">**5. Deep Learning II**")
    st.text("")
    image1 = Image.open('Deep_LearningII.png')
    st.image(image1,width=width)
    
with col12:
    st.markdown(">**6. PLN e Reconhecimento de Voz**")
    image1 = Image.open('Cert_PNL_FIA.jpg')
    st.image(image1,width=width)
    
    
col13, col14, col15  = st.columns(3)
width=230
with col13:
    st.markdown(">**7. Sistemas Cognitivos**")
    st.text("")
    image2 = Image.open('cert_sist_cognitivos.jpg')
    st.image(image2,width=width)
with col14:
    st.markdown(">**7. Análise de Grafos para Big Data**")
    image1 = Image.open('Cert_Grafos.jpg')
    st.image(image1,width=width)
    
with col15:
    st.markdown(">**7. Visão Computacional e Reconhecimento de Imagem**")
    image1 = Image.open('Cert_VisaoFIA.jpg')
    st.image(image1,width=width)

st.markdown("----------------")   
st.markdown("**Formação Cientista de Dados...**")
image1 = Image.open('Cert_FCD.png')
st.image(image1,width=500)

st.markdown("**... que é composta pelos cursos:**")

col1, col2, col3  = st.columns(3)
width=230
with col1:
    st.markdown(">**1. Big Data Analytics com R e Microsoft Azure ML**")
    image1 = Image.open('Cert_R.png')
    st.image(image1,width=width)
with col2:
    st.markdown(">**2. Big Data Real-Time Analytics com Python e Spark**")
    image1 = Image.open('Cert_Python_Spark.png')
    st.image(image1,width=width)
    
with col3:
    st.markdown(">**3. Engenharia de Dados com Hadoop e Spark**")
    image1 = Image.open('Cert_Haddop.png')
    st.image(image1,width=width)
    
col4, col5, col6  = st.columns(3)
width=230
with col4:
    st.markdown(">**4. Machine Learning**                             ")
    st.text("")
    image1 = Image.open('Cert_ML.png')
    st.image(image1,width=width)
with col5:
    st.markdown(">**5. Business Analytics**                            ")
    st.text("")
    image1 = Image.open('Cert_Business.png')
    st.image(image1,width=width)
    
with col6:
    st.markdown(">**6. Visualização de dados e Design de Dashboards**")
    image1 = Image.open('Cert_Dataviz.png')
    st.image(image1,width=width)

st.markdown("----------------")   
st.markdown("**SQL Para Data Science**")
image1 = Image.open('Cert_SQL.png')
st.image(image1,width=500)

st.markdown("----------------")   
st.markdown("**Microsoft Power BI Para Data Science 3.0**")
image1 = Image.open('Power_BI_3.png')
st.image(image1,width=500)

st.markdown("**Microsoft Power BI Para Data Science 2.0**")
image1 = Image.open('Power_BI.png')
st.image(image1,width=500)

st.markdown("----------------")   
st.markdown("**Introdução ao Sistema Operacional Linux**")
image1 = Image.open('Cert_Linux_Intro.png')
st.image(image1,width=500)

st.markdown("----------------")   
st.markdown("**Análise Estatística e Modelagem Preditiva de Séries Temporais**")
image1 = Image.open('Cert_Ser_Temp.png')
st.image(image1,width=500)

st.markdown("----------------")   
st.markdown("**Python Fundamentos para Análise de Dados**")
image1 = Image.open('Cert_Python_Intro.png')
st.image(image1,width=500)

st.markdown("----------------")   
st.markdown("**Big Data Fundamentos**")
image1 = Image.open('Cert_Intro_BD.png')
st.image(image1,width=500)

st.markdown("----------------")   
st.markdown("**Introdução à Ciência de Dados**")
image1 = Image.open('Cert_Intro_CD.png')
st.image(image1,width=500)
st.markdown("----------------")   




