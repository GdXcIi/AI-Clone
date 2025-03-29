import streamlit as st
from openai import OpenAI

def Accueil():
    columns = st.columns(3)
    with columns[1]:
        st.image("img/logo.png", use_container_width=True)
    
    st.title("Bienvenue sur AI Clone !")
    st.write("_Effectuez vos requêtes API avec une belle interface graphique, simple et épurée, optimisée pour cela !_")