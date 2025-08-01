import streamlit as st
from wiki_utils import get_wiki_text
from openai import OpenAI
import os

# Configurazione interfaccia Streamlit
st.set_page_config(page_title="GAM Helper", layout="wide")
st.title("🤖 Agente GAM – Google Apps Manager")

# Inizializza client OpenAI
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# Input utente
query = st.text_input("Scrivi una domanda sulla sintassi o i comandi di GAM:")

# Quando viene scritta una domanda
if query:
    with st.spinner("Sto leggendo la wiki GAM..."):
        context = get_wiki_text()

        response = client.chat.completions.create(
            model="gpt-4",
            messages=[
                {
                    "role": "system",
                    "content": "Sei un esperto di Google Apps Manager (GAM). Rispondi solo usando la wiki ufficiale."
                },
                {
                    "role": "user",
                    "content": f"La wiki dice:\n{context}\n\nDomanda: {query}"
                }
            ],
            temperature=0.2
        )

        st.markdown("### 💬 Risposta")
        st.write(response.choices[0].message.content)
