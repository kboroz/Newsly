import streamlit as st
from data.news_fetcher import fetch_news_text
from utils.embeddings import build_vectorstore
from agents.qa_agent import build_qa_chain
from agents.summarizer import summarize_news
from utils.text_to_speech import text_to_audio

import streamlit as st
import os  # Make sure to import the os module
from data.news_fetcher import fetch_news_text
from utils.embeddings import build_vectorstore
from agents.qa_agent import build_qa_chain
from agents.summarizer import summarize_news
from utils.text_to_speech import text_to_audio

st.set_page_config(page_title="Deutschlandfunk News Agent", layout="centered")
st.title("📰 Deutschlandfunk Nachrichtenassistent")

news_text = fetch_news_text()
vectorstore = build_vectorstore(news_text)
qa_chain = build_qa_chain(vectorstore)

if news_text:
    with st.expander("📝 Zusammenfassung anzeigen"):
        summary = summarize_news(news_text)
        st.markdown(summary)

st.subheader("❓ Stelle deine Frage")
user_question = st.text_input("Frage", placeholder="Was ist diese Woche passiert?")

if user_question and qa_chain:
    with st.spinner("🤖 Denke nach..."):
        try:
            answer = qa_chain.run(user_question)
            st.success(answer)
            lang = st.selectbox("Sprache der Audioausgabe", ["de", "en"], index=0)
            audio_path = text_to_audio(answer, lang=lang)
            with open(audio_path, "rb") as f:
                st.audio(f.read(), format="audio/mp3")
        finally:
            if audio_path:
                os.unlink(audio_path)

st.markdown("---")
st.caption("Made with 🧠 by ChatGPT | Quelle: Deutschlandfunk")

