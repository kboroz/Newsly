from langchain.chains import RetrievalQA
#from langchain.llms import Ollama
from langchain_community.llms import Ollama
from streamlit import cache_resource
from config.config import OLLAMA_MODEL_NAME


@cache_resource
def build_qa_chain(_vectorstore):
    if _vectorstore is None:
        return None
    llm = Ollama(model=OLLAMA_MODEL_NAME, temperature=0.5)
    return RetrievalQA.from_chain_type(
        llm=llm,
        chain_type="stuff",
        retriever=_vectorstore.as_retriever()
    )



