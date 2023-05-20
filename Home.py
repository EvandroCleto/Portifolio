import streamlit as st
from PIL import Image
import streamlit.components.v1 as components

st.set_page_config(
    page_title="Evandro Cleto Portifolio",
    page_icon="🏚️",
)



image = Image.open('Home_DSr.jpg')
st.image(image,width=620)

st.markdown("## Evandro Eulálio Cleto")
st.markdown("### Cientista de dados | Consultor ERP Totvs Protheus")





