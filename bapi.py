from collections import Counter
import string
import requests
from bs4 import BeautifulSoup
import re
from words import perguntas, artigos, sers

def buscar_api(termo):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0 Safari/537.36'
    }
    response = requests.get(f'https://pt.wikipedia.org/wiki/{termo}', headers=headers)
    soup = BeautifulSoup(response.text, 'html.parser')
    resultado_wiki = soup.find_all('li', class_='b_algo')
    resumir(termo, resultado_wiki)
    print(resumo)

def resumir(termo, pesquisa):
    ser_pattern = "|".join(re.escape(s) for s in sers)
    artigo_pattern = "|".join(re.escape(a) for a in artigos)
    padrao = rf"{re.escape(termo)} (?:{ser_pattern}) (?:{artigo_pattern}) (\w+)"
    match = re.search(padrao, pesquisa)
    if match:
        nome = match.group(1)
        global resumo
        resumo = f'{termo} {ser_pattern} {artigo_pattern} {nome}'