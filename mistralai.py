import streamlit as st
import requests
import json
import time

def Mistral():
    st.title("Chat avec Mistral AI")
    st.write("_Discutez dès maintenant avec le meilleur équivalent français à ChatGPT !_")

    # Initialisation de l'état de session pour stocker les messages
    if "messages" not in st.session_state:
        st.session_state.messages = []

    # Affichage des messages précédents
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    # Entrée utilisateur
    prompt = st.chat_input("Qu'est-ce qui vous amène dans le coin ?")
    if prompt:
        # Ajout du message de l'utilisateur à l'historique
        st.session_state.messages.append({"role": "user", "content": prompt})
        with st.chat_message("user"):
            st.markdown(prompt)

        # Préparation de la requête à l'API Mistral AI
        headers = {
            "Authorization": f"Bearer {st.secrets['MISTRAL_API_KEY']}",
            "Content-Type": "application/json"
        }
        data = {
            "model": "mistral-medium",  # Remplacez par le modèle approprié si nécessaire
            "messages": st.session_state.messages
        }

        # Envoi de la requête à l'API
        response = requests.post("https://api.mistral.ai/v1/chat/completions", headers=headers, json=data)

        if response.status_code == 200:
            json_response = response.json()
            assistant_message = json_response["choices"][0]["message"]["content"]
            st.session_state.messages.append({"role": "assistant", "content": assistant_message})

            # Affichage de la réponse de l'assistant mot par mot
            with st.chat_message("assistant"):
                response_container = st.empty()
                full_response = ""
                for word in assistant_message.split():
                    full_response += word + " "
                    response_container.markdown(full_response)
                    time.sleep(0.05)  # Délai pour l'effet de saisie
        else:
            st.error(f"Erreur {response.status_code} : {response.text}")

if __name__ == "__main__":
    Mistral()
