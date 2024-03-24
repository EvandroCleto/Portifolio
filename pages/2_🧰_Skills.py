import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(
    page_title="Skills",
    page_icon="🧰",
)

st.markdown("## Estes são os skills em Data Science que domino:")

col1, col2 = st.columns(2)

with col1:
    
   st.slider("SQL",0,100, 95)

with col2:
    r = st.slider('Python', 0, 100, 90)
    
    
col3, col4 = st.columns(2)

with col3:
    ml = st.slider('Machine Learning', 0, 100, 90)

with col4:
    prompt = st.slider('Prompt Engineering', 0, 100, 90)

col5, col6 = st.columns(2)

with col5:
    llm = st.slider('LLM', 0, 100, 90)
    
with col6:
    rl = st.slider('Linguagem R', 0, 100, 90)
    
col7, col8 = st.columns(2)

with col7:
   spark = st.slider('Apache Spark', 0, 100, 80)

with col8:
    git = st.slider('Git/GitHub', 0, 100, 80)

col9, col10 = st.columns(2)

with col9:
    gcp = st.slider('GCP (VertexIA | Big Query)', 0, 100, 80)    
    
with col10:
    aml = st.slider('Azure Machine Learning', 0, 100, 80)
    
col11, col12 = st.columns(2) 

with col11:
    linux = st.slider('Linux', 0, 100, 80)

with col12:
    powerbi = st.slider('Power BI', 0, 100, 80)

col13, col14 = st.columns(2) 

with col13:
    haddop = st.slider('Apache Hadoop', 0, 100, 75)

with col14:
    vm = st.slider('Oracle VM', 0, 100, 75)

col15, col16 = st.columns(2) 

with col15:
    pnl = st.slider('PNL', 0, 100, 75)

with col16:
    scrum = st.slider('Scrum', 0, 100, 75)
    
col17,col18 = st.columns(2) 

with col17:
    docker = st.slider('Docker', 0, 100, 75)

with col18:
    dl = st.slider('Deep Learning', 0, 100, 75)
    
col19,col20 = st.columns(2) 
    
with col19:
    pt = st.slider('PyTorch', 0, 100, 75)

with col20:
    ts = st.slider('TensorFlow', 0, 100, 75)
        
col21,col22 = st.columns(2) 
    
with col21:
    tr = st.slider('Transformers', 0, 100, 75)
    
with col22:
    hf = st.slider('Hugging Face', 0, 100, 75)  

col23,col24 = st.columns(2) 
    
with col23:
    vector = st.slider('Vector DB', 0, 100, 75)
    
with col24:
    rag = st.slider('RAG', 0, 100, 60)  

col25,col26 = st.columns(2) 
    
with col25:
    vector = st.slider('Neo4j', 0, 100, 60)
    
with col26:
    rag = st.slider('Cypher', 0, 100, 60)  