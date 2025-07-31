A modular application that scrapes, processes, summarizes, and vocalizes news content using LangChain, Hugging Face, FAISS, and gTTS.

📄 build_vectorstore(text)

Splits the input news text into manageable chunks using RecursiveCharacterTextSplitter, then embeds them with HuggingFaceEmbeddings (all-MiniLM-L6-v2) and stores them in a FAISS vectorstore for semantic retrieval.
Streamlit’s @cache_resource decorator is used to cache the result efficiently.
🔊 text_to_audio(text, lang="de")

Converts a text string into an MP3 audio file using Google Text-to-Speech (gTTS). Returns the path to a temporary audio file that can be played or downloaded.
