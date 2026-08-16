import random
import string
from words import saudacoes, saudacoes_, saudacoes_e, perguntas
import requests
from bs4 import BeautifulSoup
import os
from collections import Counter

os.system('cls')
while True:
    vc = input('você: ')
    vc_clean = vc.translate(str.maketrans('', '', string.punctuation))
    palavras = vc_clean.split()
    vc_no = [p for p in palavras if p != "monkey"]
    vc_no_monkey = ' '.join(vc_no)
    if any (palavra in saudacoes or palavra in saudacoes_ or palavra in saudacoes_e for palavra in palavras):
        saudacao = random.choice(saudacoes)
        saudacao_e = random.choice(saudacoes_e)
        saudacao_ = random.choice(saudacoes_)
        print(f'MONKEY: {saudacao}, {saudacao_}!')
        continue
    else:
        headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0 Safari/537.36'
        }
        response = requests.get('https://www.bing.com/search', params={'q': f'{vc_no_monkey}'}, headers=headers)
        soup = BeautifulSoup(response.text, 'html.parser')
        resultados = soup.find_all('li', class_='b_algo')
        todo_texto = []
        for r in resultados:
           titulo = r.find('h2')
           link = r.find('a')
           print(titulo.get_text() if titulo else None)
           print(link['href'] if link else None)
           print('---')