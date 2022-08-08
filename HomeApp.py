import streamlit as st
#from constant import *
from PIL import Image
import streamlit.components.v1 as components

st.set_page_config(
    page_title="Hello",
    page_icon="👋",
)

st.sidebar.caption('Meus contatos são:')
with st.sidebar:
        #components.html(embed_component['linkedin'],height=310)
        components.html("""<script src="https://platform.linkedin.com/badges/js/profile.js" async defer type="text/javascript"></script>
       <div class="badge-base LI-profile-badge" data-locale="en_US" data-size="medium" data-theme="light" data-type="VERTICAL" data-vanity="evandro-cleto-51b49340" data-version="v1"><a class="badge-base__link LI-simple-link" href="https://br.linkedin.com/in/evandro-cleto-51b49340?trk=profile-badge">Evandro Cleto</a></div>""",height=310)
    
#st.sidebar.write('Linkdin: https://br.linkedin.com/in/evandro-cleto-51b49340')
st.sidebar.write('📧: evandrocleto74@gmail.com')
st.sidebar.write('📱: +551197069-0730')

pdfFileObj = open('CurriculoEvandroCleto.pdf', 'rb')
st.sidebar.download_button('Baixe meu CV',pdfFileObj,file_name='CurriculoEvandroCleto.pdf',mime='pdf')

st.sidebar.markdown("# Sobre mim")

col1, col2 = st.columns(2)
with col1:
   st.markdown(" Olá. Eu sou o Evandro Cleto, Data Scientist (Formado pela Data Science Academy), Consultor ERP Totvs Protheus, pai do Gabriel, Ultramaratonista amador e metido a cozinheiro(O Gabriel fala que o melhor arroz e feijão do mundo é o do Papai!!) ")
   st.markdown(" É um prazer ter a sua visita e poder compartilhar um pouco da minha experiência com voce.")
   st.markdown(" Sinta-se a vontade em me deixar um recado nos comentário.")

with col2:
    image = Image.open('Main_Photo.jpg')
    st.image(image,width=160,caption='Ultimate XC-60Km')

 #st.write("pai do Gabriel, Ultramaratonista amador e metido a cozinheiro(O Gabriel fala que o melhor arroz e feijão do mundo é o do Papai!!)")
#st.write("É um prazer ter a sua visita e poder compartilhar um pouco da minha experiência com voce.")
#st.write("Sinta-se a vontade em me deixar um recado comentário.")

#st.sidebar.success("Select a demo above.")




