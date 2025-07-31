import requests
from bs4 import BeautifulSoup
from streamlit import cache_data

dfl_url = "https://www.deutschlandfunk.de/nachrichten-100.html"

@cache_data(ttl=86400)
def fetch_news_text():
    try:
        r = requests.get(dfl_url, headers={"User-Agent": "Mozilla/5.0"}, timeout=10)
        r.raise_for_status()
        soup = BeautifulSoup(r.content, "html.parser")
        paragraphs = soup.find_all("p")
        return "\n".join(p.get_text(strip=True) for p in paragraphs if p.get_text(strip=True))
    except Exception as e:
        return ""
