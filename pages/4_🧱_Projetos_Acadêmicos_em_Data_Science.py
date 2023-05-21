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
        image = Image.open('Logo_R.png')
        st.image(image,width=80)


    with col5:
       
        image = Image.open('D:\Portifolio\Page_4-Projetos_Academicos\imagens\Ser_Temp_R.png')
        st.image(image,width=350)

    
    col6 = st.columns(1)
    
    st.markdown("**Resumo:** ")
    st.markdown(" Projeto de séries temporais em linguagem R para analisar dados do mercado financeiro.")
    st.markdown("**Acesse o fonte do projeto aqui:** https://github.com/EvandroCleto/Portifolio/blob/main/Page_4-Projetos_Academicos/fontes/11-Big-Data-na-Pratica5_Ser_Temp.R")
    
with st.container():

    st.markdown("----------------")    
    
    col7, col8 = st.columns(2)

    with col7:
    
        st.markdown("### Projeto Teste A/B.")
        st.image(Image.open('Logo_Python.png'),width=60)
        st.image(Image.open('Logo_Scipy.png'),width=70)
        st.image(Image.open('Logo_NumPy.png'),width=80)
        st.image(Image.open('Logo_Pandas.png'),width=80)
        st.image(Image.open('Logo_matplot.png'),width=80)


    with col8:
        st.text("")
        st.text("")
        st.text("")
        st.text("")
        image = Image.open('D:\Portifolio\Page_4-Projetos_Academicos\imagens\TesteAB.png')
        st.image(image,width=350)

    
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
        st.image(Image.open('Logo_Python.png'),width=100)
        st.image(Image.open('Logo_Spark.png'),width=100)

    with col11:
        st.text("")
        st.text("")
        st.text("")
        image = Image.open('D:\Portifolio\Page_4-Projetos_Academicos\imagens\ML_Spark.png')
        st.image(image,width=350)

    
    col12 = st.columns(1)
    
    st.markdown("**Resumo:** ")
    st.markdown(" Projeto para criação de modelos de Machine Learning com o PySpark, demonstrando todo o pipeline de Machine Learning para ambientes distribuídos e indicando características, vantagens, desvantagens e aplicações de alguns dos principais algoritmos de aprendizado de máquina, além de abordar temas como padronização, transformação de variáveis, redução de dimensionalidade com PCA e diversas tarefas de pré-processamento de dados.")
    st.markdown("**Acesse o fonte do projeto aqui:** https://github.com/EvandroCleto/Portifolio/blob/main/Page_4-Projetos_Academicos/fontes/Spark_ML_Regrassao.ipynb")

with st.container():

    st.markdown("----------------")    
    
    col13, col14 = st.columns(2)

    with col13:
    
        st.markdown("### Sistema de Recomendação em Tempo Real com Machine Learning, PySpark, Spark Streaming e Kafka.")
        st.image(Image.open('Logo_Python.png'),width=50)
        st.image(Image.open('Logo_Spark.png'),width=70)
        st.image(Image.open('Logo_Kafka.png'),width=70)
        st.image(Image.open('D:\Portifolio\Page_4-Projetos_Academicos\imagens\Logo_Spotify.png'),width=40)
        

    with col14:
        st.text("")
        st.text("")
        st.text("")
        st.text("")
        st.text("")
        st.text("")
        st.text("")
        image = Image.open('D:\Portifolio\Page_4-Projetos_Academicos\imagens\Spotify.png')
        st.image(image,width=450)

    
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
        st.image(Image.open('Logo_R.png'),width=80)
  
    with col17:

        image = Image.open('D:\Portifolio\Page_4-Projetos_Academicos\imagens\Deep_L_Classif.png')
        st.image(image,width=450)

    
    col18 = st.columns(1)
    
    st.markdown("**Resumo:** ")
    st.markdown(" Projeto para Classificão de Imagens usando Deep Learning em Linguagem R.")
    st.markdown("**Acesse o fonte do projeto aqui:** https://github.com/EvandroCleto/Portifolio/blob/main/Page_4-Projetos_Academicos/fontes/Deep_Learning_Classific.R")

with st.container():

    st.markdown("----------------")    
    
    col19, col20 = st.columns(2)

    with col19:
    
        st.markdown("### Rede Neural com TensorFlow Para Classificação de Imagens de Vestuário.")
        st.image(Image.open('Logo_Python.png'),width=70)
        st.image(Image.open('Logo_Tesnsoflow.png'),width=80)
    with col20:

        image = Image.open('D:\Portifolio\Page_4-Projetos_Academicos\imagens\Rede_Neural.png')
        st.image(image,width=450)

    
    col21 = st.columns(1)
    
    st.markdown("**Resumo:** ")
    st.markdown(" Neste Projeto foi construida uma rede neural artificial com TensorFlow para classificação de imagens, especificamente classificação de imagens de roupas e acessórios.")
    st.markdown("**Acesse o fonte do projeto aqui:** https://github.com/EvandroCleto/Portifolio/blob/main/Page_4-Projetos_Academicos/fontes/Rede_Neural_TensorFlow.ipynb")

with st.container():

    st.markdown("----------------")    
    
    col22, col23 = st.columns(2)

    with col22:
    
        st.markdown("### Prevendo os Efeitos do Consumo de Álcool em Doenças do Fígado")
        st.image = Image.open('Logo_R.png')

    with col23:

        image = Image.open('D:\Portifolio\Page_4-Projetos_Academicos\imagens\Previsao_Doencas_Figado.png')
        st.image(image,width=450)

    
    col24 = st.columns(1)
    
    st.markdown("**Resumo:** ")
    st.markdown(" Neste estudo de caso foi usado um modelo de rede neural para prever os efeitos do consumo de álcool em doenças do fígado. ")
    st.markdown("**Acesse o fonte do projeto aqui:** https://github.com/EvandroCleto/Portifolio/blob/main/Page_4-Projetos_Academicos/fontes/Rede_Neural_TensorFlow.ipynb")