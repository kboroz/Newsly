# This project is part of the OpenCampus course: 

"From LLMs to AI Agents" (https://edu.opencampus.sh/course/563) 

The goal is a dynamic news assistant that not only fetches news from Deutschlandfunk but also processes it intelligently. 

It provides the user with a concise summary and an interactive question-answer function.

The language model used is Llama3.2 – which can be replaced with other models depending on the available hardware.

# Main Components

    config.py: Central management of important configuration parameters such as API tokens and model names.

    data/news_fetcher.py: This part of the code actively fetches the latest news from Deutschlandfunk and prepares it for further processing.

    utils/embeddings.py: Converts the fetched text into a high-performance vector store, optimized for later use in the question-answer chain.

    agents/qa_agent.py: Builds an intelligent question-answer pipeline that uses the vector store to deliver precise and fast answers.

    agents/summarizer.py: Summarizes the fetched news text concisely so users can get a quick overview.

    utils/text_to_speech.py: Converts text into audio, making the answers not only readable but also audible.

    app.py: The main application uses Streamlit to provide a user-friendly and interactive interface. It fetches news, shows a summary, and allows users to ask questions.

# How It Works

    News Fetching: The app proactively fetches the latest news from Deutschlandfunk and stores it in a variable.

    Vector Store: The fetched text is converted into a vector store to enable efficient search and querying. This ensures fast and accurate answers.

    Summarization: The fetched text is automatically summarized and displayed to the user, providing a quick overview.

    Question-Answer Function: Users can ask questions, which are answered intelligently by the QA pipeline. The answer is provided both as text and audio, enhancing usability.

# User Interface

The user interface is built with Streamlit and offers the following features:

    Display of a concise summary of the news.

    Input field for user questions to encourage interaction.

    Display of answers and playback of the audio output for a more pleasant user experience.

# Linux Command Line Instructions to Run the Code:

cd Downloads/
cd newsly/

python3 -m venv .venv
source .venv/bin/activate

pip install --upgrade pip
pip install -r requirements.txt
pip install -U langchain-community

ollama pull llama3.2

touch agents/__init__.py config/__init__.py data/__init__.py utils/__init__.py

streamlit run app.py
