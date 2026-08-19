import random
import string
from words import saudacoes_, saudacoes_e, perguntas, criações, artigos, sers, frases_de_ajuda, palavroes, resp_palavrao
import requests
from bs4 import BeautifulSoup
import os
from collections import Counter
from datetime import date, datetime
from login import novo_usuario

hora_atual = datetime.now().hour
hoje = date.today()
dia = hoje.day
mes = hoje.month

os.system('cls')
while True:
    vc = input('você: ')
    vc_clean = vc.translate(str.maketrans('', '', string.punctuation))
    palavras = vc_clean.split()
    vc_no = [p for p in palavras if p != "monkey"]
    vc_no_monkey = ' '.join(vc_no)
    if any (saudacao_ in vc_clean or saudacao_e in vc_clean for saudacao_ in saudacoes_ for saudacao_e in saudacoes_e):
        if 5 <= hora_atual < 12:
            saudacao = "Bom dia"
        elif 12 <= hora_atual < 19:
            saudacao = "Boa tarde"
        else:
            saudacao = "Boa noite"
        saudacao_e = random.choice(saudacoes_e)
        saudacao_ = random.choice(saudacoes_)
        frase = random.choice(frases_de_ajuda)
        print(f'MONKEY: {saudacao}, {novo_usuario}, {saudacao_}! {frase}')
        continue
    elif any (pergunta in vc_clean for pergunta in perguntas) and (sers in vc_clean for pergunta in perguntas):
        headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0 Safari/537.36'
        }
        termo = ' '.join(p for p in palavras if p not in perguntas and p not in sers and p not in artigos)
        response = requests.get(f'https://pt.wikipedia.org/wiki/{termo.replace(" ", "_")}', headers=headers)
        soup = BeautifulSoup(response.text, 'html.parser')
        todo_texto = []
        for p in soup.find_all('p'):
            print(p.get_text())
    elif any (palavrao in vc_clean for palavrao in palavroes):
        resposta = random.choice(resp_palavrao)
        print(f'MONKEY: {resposta}')
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