import requests
from bs4 import BeautifulSoup

def fetch_full(url):
    try:
        html = requests.get(url).text
        soup = BeautifulSoup(html, "html.parser")
        content = soup.select_one("#js_content")
        return str(content) if content else ""
    except:
        return ""