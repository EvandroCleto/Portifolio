import streamlit as st
import streamlit.components.v1 as components
from PIL import Image

st.set_page_config(
    page_title="Idiomas",
    page_icon="👅",
)


with st.container():
    
    col1, col2, col3 = st.columns(3)

    with col1:
        
        st.markdown("")

    with col2:
        image = Image.open('Flag_of_Canada.png')
        st.image(image,width=250)
    
    with col3:
        
        st.markdown("")

st.markdown("###### Em 2007 decidi melhorar minha proficiência no Inglês e me mudei para Toronto no Canadá, onde fiquei até 2008 estudando esse idioma e fazendo alguns trabalhos na área da construção para custear minha estadia por lá.")
st.markdown("###### Entre 2016 a 2018 voltei a morar no Canadá, dessa vez em Montreal e aproveitei para aprender o idioma Francês. Também tive a oportunidade de trabalhar na WADA(World Anti Doping Agency) fazendo serviços administrativos, onde coloquei em prática o que aprendi sobre Inglês e Francês.")

st.markdown("###### E por falar em Canadá, em nenhuma destas vezes encontrei a Luisa!!")


col4, col5 = st.columns(2)

with col4:
    
   st.slider("Inglês",0,100, 90)

with col5:
   st.slider('Francês', 0, 100, 50)
    
    




