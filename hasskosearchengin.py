import requests
from bs4 import BeautifulSoup
from urllib.parse import quote

def search_duckduckgo(query):
    url = f"https://html.duckduckgo.com/html/?q={quote(query)}"
    headers = {'User-Agent': 'Mozilla/5.0'}
    r = requests.get(url, headers=headers)
    soup = BeautifulSoup(r.text, 'html.parser')
    results = [a['href'] for a in soup.select('.result__a')]
    return results[:5]

def search_bing(query):
    url = f"https://www.bing.com/search?q={quote(query)}"
    r = requests.get(url)
    soup = BeautifulSoup(r.text, 'html.parser')
    results = [a['href'] for a in soup.select('li.b_algo h2 a')]
    return results[:5]

def search_yahoo(query):
    url = f"https://search.yahoo.com/search?p={quote(query)}"
    r = requests.get(url)
    soup = BeautifulSoup(r.text, 'html.parser')
    results = [a['href'] for a in soup.select('h3.title a')]
    return results[:5]

def search_qwant(query):
    url = f"https://lite.qwant.com/?q={quote(query)}"
    r = requests.get(url)
    soup = BeautifulSoup(r.text, 'html.parser')
    results = [a['href'] for a in soup.select('a.result__a')]
    return results[:5]

def search_ecosia(query):
    url = f"https://www.ecosia.org/search?q={quote(query)}"
    r = requests.get(url)
    soup = BeautifulSoup(r.text, 'html.parser')
    results = [a['href'] for a in soup.select('a.result-title')]
    return results[:5]

def search_mojeek(query):
    url = f"https://www.mojeek.com/search?q={quote(query)}"
    r = requests.get(url)
    soup = BeautifulSoup(r.text, 'html.parser')
    results = [a['href'] for a in soup.select('.result a')]
    return results[:5]

def main():
    query = input("Enter search query: ")
    engines = {
        'DuckDuckGo': search_duckduckgo,
        'Bing': search_bing,
        'Yahoo': search_yahoo,
        'Qwant': search_qwant,
        'Ecosia': search_ecosia,
        'Mojeek': search_mojeek
    }

    for name, func in engines.items():
        print(f"\n{name} Results:")
        try:
            results = func(query)
            for url in results:
                print(" -", url)
        except Exception as e:
            print(f"Error fetching from {name}: {e}")

if __name__ == "__main__":
    main()
