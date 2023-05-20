import streamlit as st
from PIL import Image
import streamlit.components.v1 as components

st.set_page_config(
    page_title="Contatos",
    page_icon="📡",
)

st.write('### **Como me encontrar:**')

#components.html(embed_component['linkedin'],height=310)
components.html("""<script src="https://platform.linkedin.com/badges/js/profile.js" async defer type="text/javascript"></script>
<div class="badge-base LI-profile-badge" data-locale="en_US" data-size="medium" data-theme="light" data-type="VERTICAL" data-vanity="evandro-cleto-51b49340" data-version="v1"><a class="badge-base__link LI-simple-link" href="https://br.linkedin.com/in/evandro-cleto-51b49340?trk=profile-badge"></a></div>""",height=250)
    
#st.sidebar.write('Linkdin: https://www.linkedin.com/in/evandro-cleto-51b49340/?locale=pt_BR&original_referer=')
st.write('📧: **evandrocleto74@gmail.com**')
st.write('📱: **+551197069-0730**')

pdfFileObj = open('Currículo_Evandro_Cleto.pdf', 'rb')
st.download_button('Baixe meu CV',pdfFileObj,file_name='Currículo_Evandro_Cleto.pdf',mime='pdf')

st.write('#### Será um prazer receber seu contato.')