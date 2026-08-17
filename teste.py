import requests
from bs4 import BeautifulSoup

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0 Safari/537.36'
}

response = requests.get('https://www.bing.com/search', params={'q': 'o corinthinas joga hoje?'}, headers=headers)
soup = BeautifulSoup(response.text, 'html.parser')
resultados = soup.find_all('li', class_='b_algo')

for r in resultados:
    titulo = r.find('h2')
    link = r.find('a')
    print(titulo.get_text() if titulo else None)
    print(link['href'] if link else None)
    print('---')
    #Guimmel Apollo
    import os