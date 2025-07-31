This utility fetches and parses the latest news from Deutschlandfunk Nachrichten:

    fetch_news_text()
    Scrapes paragraph text from the Deutschlandfunk news page using requests and BeautifulSoup.
    Results are cached for 24 hours with Streamlit's @cache_data(ttl=86400) to reduce load and improve performance.

Robust error handling ensures graceful fallback if the request fails.
