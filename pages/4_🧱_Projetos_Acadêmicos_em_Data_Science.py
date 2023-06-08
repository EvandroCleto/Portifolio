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

st.markdown("Aqui estão alguns dos projetos de Data Science que estudei durante a Formação Cientista de Dados na Data Science Academy(https://www.datascienceacademy.com.br/bundle/formacao-cientista-de-dados).")

with st.container():

    st.markdown("----------------")    
    
    col4, col5 = st.columns(2)

    with col4:
        
        st.markdown("### Análise de Séries Temporais no Mercado Financeiro.")
        image1 = Image.open('Logo_R.png')
        st.image(image1,width=80)


    with col5:
        
        image2 = Image.open('Ser_Temp_R.png')
        st.image(image2,width=350)

    
    col6 = st.columns(1)
    
    st.markdown("**Resumo:** ")
    st.markdown(" Projeto de séries temporais em linguagem R para analisar dados do mercado financeiro.")
    st.markdown("**Acesse o fonte do projeto aqui:** https://github.com/EvandroCleto/Portifolio/blob/main/Page_4-Projetos_Academicos/fontes/11-Big-Data-na-Pratica5_Ser_Temp.R")
    
with st.container():

    st.markdown("----------------")    
    
    col7, col8 = st.columns(2)

    with col7:
    
        st.markdown("### Projeto Teste A/B.")
        image1 = Image.open('Logo_Python.png')
        st.image(image1,width=60)
        image2 = Image.open('Logo_Scipy.png')
        st.image(image2 ,width=70)
        image3 = Image.open('Logo_NumPy.png')
        st.image(image3,width=80)
        image4 = Image.open('Logo_Pandas.png')
        st.image(image4,width=80)
        image5 = Image.open('Logo_matplot.png')
        st.image(image5,width=80)


    with col8:
        st.text("")
        st.text("")
        st.text("")
        st.text("")
        
        image6 = Image.open('TesteAB.png')
        st.image(image6,width=350)

    
    col9 = st.columns(1)
    
    st.markdown("**Resumo:** ")
    st.markdown(" O Teste A/B, ou teste de divisão, é um método eficaz em Marketing Digital, como técnica de otimização, para tentar gradualmente aumentar as conversões do funil de vendas (contatos ou vendas). Ou ainda melhorar outras fases iniciais como, por exemplo, taxa de cliques ou taxa de rejeição.")
    st.markdown("Um Teste A/B consiste em testar duas diferentes estratégias em um grupo específico.")
    st.markdown("**Acesse o fonte do projeto aqui:** https://github.com/EvandroCleto/Portifolio/blob/main/Page_4-Projetos_Academicos/fontes/Teste_A_B.ipynb")
    
with st.container():

    st.markdown("----------------")    
    
    col10, col11 = st.columns(2)

    with col10:
    
        st.markdown("### Projeto Machine Learning com PySpark.")
        image1 = Image.open('Logo_Python.png')
        st.image(image1,width=100)
        
        image2 = Image.open('Logo_Spark.png')
        st.image(image2,width=100)

    with col11:
        st.text("")
        st.text("")
        st.text("")
        image3 = Image.open('ML_Spark.png')
        st.image(image3,width=350)

    
    col12 = st.columns(1)
    
    st.markdown("**Resumo:** ")
    st.markdown(" Projeto para criação de modelos de Machine Learning com o PySpark, demonstrando todo o pipeline de Machine Learning para ambientes distribuídos e indicando características, vantagens, desvantagens e aplicações de alguns dos principais algoritmos de aprendizado de máquina, além de abordar temas como padronização, transformação de variáveis, redução de dimensionalidade com PCA e diversas tarefas de pré-processamento de dados.")
    st.markdown("**Acesse o fonte do projeto aqui:** https://github.com/EvandroCleto/Portifolio/blob/main/Page_4-Projetos_Academicos/fontes/Spark_ML_Regrassao.ipynb")

with st.container():

    st.markdown("----------------")    
    
    col13, col14 = st.columns(2)

    with col13:
    
        st.markdown("### Sistema de Recomendação em Tempo Real com Machine Learning, PySpark, Spark Streaming e Kafka.")
        image1 = Image.open('Logo_Python.png')
        st.image(image1,width=50)
        image2 = Image.open('Logo_Spark.png')
        st.image(image2,width=70)
        image3 = Image.open('Logo_Kafka.png')
        st.image(image3,width=70)
        image4 = Image.open('Logo_Spotify.png')
        st.image(image4,width=40)
        

    with col14:
        st.text("")
        st.text("")
        st.text("")
        st.text("")
        st.text("")
        st.text("")
        st.text("")
        image5 = Image.open('Spotify.png')
        st.image(image5,width=450)

    
    col15 = st.columns(1)
    
    st.markdown("**Resumo:** ")
    st.markdown(" Neste projeto foi desenvolvido um Sistema de Recomendação em tempo real para recomendar músicas de acordo com as likes do usuários em suas músicas preferidas no Spotify.")
    st.markdown(" Para coletar a lista de músicas preferidas é realizado conexão na API do Spotify.")
    st.markdown("**Acesse o fonte da parte 1 do projeto aqui:** https://github.com/EvandroCleto/Portifolio/blob/main/Page_4-Projetos_Academicos/fontes/Recomendacao_Spotify_P1.ipynb")
    st.markdown("**Acesse o fonte da parte 2 do projeto aqui:** https://github.com/EvandroCleto/Portifolio/blob/main/Page_4-Projetos_Academicos/fontes/Recomendacao_Spotify_P2.ipynb")
    
with st.container():

    st.markdown("----------------")    
    
    col16, col17 = st.columns(2)

    with col16:
    
        st.markdown("### Deep Learning em R para Classificão de Imagens.")
        image1 = Image.open('Logo_R.png')
        st.image(image1,width=80)
  
    with col17:

        image2 = Image.open('Deep_L_Classif.png')
        st.image(image2,width=450)

    
    col18 = st.columns(1)
    
    st.markdown("**Resumo:** ")
    st.markdown(" Projeto para Classificão de Imagens usando Deep Learning em Linguagem R.")
    st.markdown("**Acesse o fonte do projeto aqui:** https://github.com/EvandroCleto/Portifolio/blob/main/Page_4-Projetos_Academicos/fontes/Deep_Learning_Classific.R")

with st.container():

    st.markdown("----------------")    
    
    col19, col20 = st.columns(2)

    with col19:
    
        st.markdown("### Rede Neural com TensorFlow Para Classificação de Imagens de Vestuário.")
        image1 = Image.open('Logo_Python.png')
        st.image(image1,width=70)
        image2 = Image.open('Logo_Tensorflow.png')
        st.image(image2,width=80)
    with col20:
        image3 = Image.open('Rede_Neural.png')
        st.image(image3,width=450)
            
    col21 = st.columns(1)
    
    st.markdown("**Resumo:** ")
    st.markdown(" Neste Projeto foi construída uma rede neural artificial com TensorFlow para classificação de imagens, especificamente classificação de imagens de roupas e acessórios.")
    st.markdown("**Acesse o fonte do projeto aqui:** https://github.com/EvandroCleto/Portifolio/blob/main/Page_4-Projetos_Academicos/fontes/Rede_Neural_TensorFlow.ipynb")

with st.container():

    st.markdown("----------------")    
    
    col22, col23 = st.columns(2)

    with col22:
    
        st.markdown("### Prevendo os Efeitos do Consumo de Álcool em Doenças do Fígado")
        image1 = Image.open('Logo_R.png')
        st.image(image1,width=80)

    with col23:
        image2 = Image.open('Prev_Doencas.png')
        st.image(image2 ,width=350)
        
    col24 = st.columns(1)
    
    st.markdown("**Resumo:** ")
    st.markdown(" Neste estudo de caso foi usado um modelo de rede neural para prever os efeitos do consumo de álcool em doenças do fígado. ")
    st.markdown("**Acesse o fonte do projeto aqui:** https://github.com/EvandroCleto/Portifolio/blob/main/Page_4-Projetos_Academicos/fontes/Previsao_Doencas_Figado.R")
    
with st.container():

    st.markdown("----------------")    
    
    col25, col26 = st.columns(2)

    with col25:
    
        st.markdown("### Análise de Preço e Análise Textual do Noticiário Econômico Para Previsão de Ativos Financeiros")
        image1 = Image.open('Logo_Python.png')
        st.image(image1,width=50)
        image2 = Image.open('Logo_NLTK.png')
        st.image(image2,width=40)
        image3 = Image.open('Logo_XGBoost.png')
        st.image(image3,width=50)
        image3 = Image.open('Logo_SciKit.png')
        st.image(image3,width=50)
        
        

    with col26:
        st.text("")
        st.text("")
        st.text("")
        st.text("")
        st.text("")

        image2 = Image.open('PNL_Merc_Fin.png')
        st.image(image2 ,width=450)
        
    col26 = st.columns(1)
    
    st.markdown("**Resumo:** ")
    st.markdown(" Neste projeto foi desenvolvido um modelo preditivo trabalhando com duas fontes de dados diferentes. Uma das fontes tem dados históricos de cotação de ativos financeiros, sobre os quais foi feita análise numérica. A outra fonte tem dados de texto do noticiário econômico, sobre os quais foi realizado análise textual. O objetivo é unir esses datsets e construir um modelo preditivo capaz de prever o valor de ativos financeiros. ")
    st.markdown("**Acesse o fonte do projeto aqui:** https://github.com/EvandroCleto/Portifolio/blob/main/Page_4-Projetos_Academicos/fontes/Cap12-Text-Analytics.ipynb")