import streamlit as st
from PIL import Image
import streamlit.components.v1 as components

st.set_page_config(
    page_title="Evandro Cleto Portifolio",
    page_icon="🏚️",
)



image = Image.open('Home_DSr.jpg')
st.image(image,width=620)

st.markdown('<div style="text-align: center;font-size: 40px"><b>Evandro Cleto</b></div>', unsafe_allow_html=True)
st.markdown('<div style="text-align: center;font-size: 23px"><b>Data Scientist Certified Specialist | Generative IA</b></div>', unsafe_allow_html=True)

st.text("")

col3, col4, col5  = st.columns(3)

with col3:
    image = Image.open('Badge_DSCS.png')
    st.image(image,width=160)

with col4:
    image = Image.open('Badge_DSCP.png')
    st.image(image,width=160)
    
with col5:
    image = Image.open('Badge_FCD.png')
    st.image(image,width=140)





