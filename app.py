"""Streamlit app that polishes therapist notes via OpenAI."""

import os
import streamlit as st
from dotenv import load_dotenv
import openai

# load .env locally if you use one; on Streamlit Cloud you'll set a secret
load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")
if not openai.api_key:
    st.warning("OPENAI_API_KEY not configured.")

st.set_page_config(page_title="Therapy Note Polisher")
st.title("📝 Therapy Note Polisher")


def polish_note(prompt: str) -> str:
    """Return a polished SOAP note for the given prompt."""
    resp = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.2,
        max_tokens=600,
    )
    return resp.choices[0].message.content.strip()


raw = st.text_area(
    "Paste your raw therapist note here:",
    height=200
)

if st.button("Polish Note"):
    if not raw.strip():
        st.error("Give me something to polish!")
    else:
        with st.spinner("Polishing…"):
            prompt = (
                "You are a clinical documentation assistant. "
                "Convert this raw therapist note into a polished SOAP note "
                "with appropriate medical terminology:\n\n"
                f"{raw}\n\nFinal Note:\n"
            )
            try:
                polished = polish_note(prompt)
                st.subheader("Polished SOAP Note")
                st.code(polished, language="markdown")
            except openai.error.OpenAIError as exc:
                st.error(f"OpenAI API call failed: {exc}")
            except Exception as exc:
                st.error(f"Unexpected error: {exc}")
