import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(
    page_title="Skills",
    page_icon="🧰",
)

st.markdown("## Estes são os skills em Data Science que desenvolvi ao longo da minha carreira.")

col1, col2 = st.columns(2)

with col1:
    
   st.slider("SQL",0,100, 95)

with col2:
    r = st.slider('Linguagem R', 0, 100, 90)
    
    
col3, col4 = st.columns(2)

with col3:
    ml = st.slider('Machine Learning', 0, 100, 90)

with col4:
    office = st.slider('Pacote Office', 0, 100, 90)

col5, col6 = st.columns(2)

with col5:
    python = st.slider('Python', 0, 100, 90)

with col6:
    spark = st.slider('Apache Spark', 0, 100, 80)

col7, col8 = st.columns(2)

with col7:
    aml = st.slider('Azure Machine Learning', 0, 100, 80)

with col8:
    stats = st.slider('Estatística', 0, 100, 80)

col9, col10 = st.columns(2)

with col9:
    git = st.slider('Git/GitHub', 0, 100, 80)

with col10:
    kanban = st.slider('Kanban', 0, 100, 80)
    
col11, col12 = st.columns(2) 

with col11:
    linux = st.slider('Linux', 0, 100, 80)

with col12:
    powerbi = st.slider('Power BI', 0, 100, 80)

col13, col14 = st.columns(2) 

with col13:
    haddop = st.slider('Apache Hadoop', 0, 100, 75)

with col14:
    dl = st.slider('Deep Learning', 0, 100, 75)

col15, col16 = st.columns(2) 

with col15:
    pnl = st.slider('PNL', 0, 100, 75)

with col16:
    scrum = st.slider('Scrum', 0, 100, 75)

