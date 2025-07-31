from langchain.llms import Ollama
from langchain.chains.question_answering import load_qa_chain
from langchain.schema import Document
#from config import OLLAMA_MODEL_NAME
OLLAMA_MODEL_NAME = "llama3.2"
from streamlit import cache_data

@cache_data
def summarize_news(text):
    if not text:
        return "Keine Nachrichten vorhanden."
    llm = Ollama(model=OLLAMA_MODEL_NAME, temperature=0.5)
    chain = load_qa_chain(llm, chain_type="stuff")
    return chain.run(input_documents=[Document(page_content=text)], question="Fasse die Nachrichten dieser Woche zusammen.")
