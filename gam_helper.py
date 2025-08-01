import streamlit as st
from wiki_utils import get_wiki_text
import openai
import os

st.set_page_config(page_title="GAM Helper", layout="wide")
st.title("🤖 Agente GAM – Google Apps Manager")

openai.api_key = os.getenv("OPENAI_API_KEY")

query = st.text_input("Scrivi una domanda sulla sintassi o i comandi di GAM:")
if query:
    with st.spinner("Sto leggendo la wiki GAM..."):
        context = get_wiki_text()
        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": "Sei un esperto di Google Apps Manager (GAM). Rispondi solo usando la wiki ufficiale."},
                {"role": "user", "content": f"La wiki dice:\n{context}\n\nDomanda: {query}"}
            ],
            temperature=0.2
        )
        st.markdown("### 💬 Risposta")
        st.write(response.choices[0].message["content"])
