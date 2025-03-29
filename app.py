import streamlit as st
from accueil import Accueil
from mistralai import Mistral
from chatgpt import ChatGPT
accueil = st.Page(Accueil, title="Accueil", icon="🏠")
mistralai = st.Page(Mistral, title="MistralAI")
openai = st.Page(ChatGPT, title="OpenAI")

pages = [accueil, mistralai, openai]
navbar = st.navigation(pages, position="sidebar", expanded=True)

navbar.run()