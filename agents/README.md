This module provides two Streamlit-cached utility functions using LangChain and Ollama:

    build_qa_chain(_vectorstore)
    Creates a RetrievalQA chain with an Ollama LLM and a vectorstore retriever for question answering over document collections.

    summarize_news(text)
    Uses a basic QA chain to summarize weekly news content from raw text input.

Both functions leverage the "stuff" chain type and integrate Streamlit caching (@cache_resource and @cache_data) for performance optimization.
