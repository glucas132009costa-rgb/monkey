import random
import string
from words import saudacoes_, saudacoes_e, perguntas, criações, artigos, sers, frases_de_ajuda, palavroes, resp_palavrao
import requests
from bs4 import BeautifulSoup
import os
from collections import Counter
from datetime import date, datetime
from login import novo_usuario, Cursor, historico
import re

resumo = None

def buscar_api(termo):
    global resumo
    resumo = None
    headers = {
        'User-Agent': 'MonkeyBot/1.0 (contato: m.o.n.k.e.y.i.a2026@gmail.com)'
    }
    params = {
        'action': 'query',
        'prop': 'extracts',
        'exintro': True,
        'explaintext': True,
        'titles': termo,
        'format': 'json',
        'redirects': 1,
    }
    try:
        response = requests.get('https://pt.wikipedia.org/w/api.php', params=params, headers=headers, timeout=10)
        response.raise_for_status()
        data = response.json()
    except (requests.RequestException, requests.exceptions.JSONDecodeError):
        return 'MONKEY: não consegui buscar isso agora.'
    paginas = data.get('query', {}).get('pages', {})
    pagina = next(iter(paginas.values()), {})
    if 'missing' in pagina or not pagina.get('extract'):
        return f'MONKEY: não encontrei nada sobre "{termo}".'
    texto = pagina['extract']
    resumir(termo, texto)
    if resumo:
        return f'MONKEY: {resumo}'
    return f'MONKEY: {texto.split(".")[0]}.'

def resumir(termo, pesquisa):
    global resumo
    ser_pattern = "|".join(re.escape(s) for s in sers)
    artigo_pattern = "|".join(re.escape(a) for a in artigos)
    padrao = rf"{re.escape(termo)} ({ser_pattern}) ({artigo_pattern}) (\w+)"
    match = re.search(padrao, pesquisa)
    if match:
        ser_encontrado, artigo_encontrado, nome = match.groups()
        resumo = f'{termo} {ser_encontrado} {artigo_encontrado} {nome}'

def salvar_cnv(vc_cnv, monkey_cnv):
    Cursor.execute("""
    INSERT INTO cnvs (você, monkey)
    VALUES (?, ?)
    """, (vc_cnv, monkey_cnv))
    historico.commit()

hora_atual = datetime.now().hour
hoje = date.today()
dia = hoje.day
mes = hoje.month

os.system('cls')
while True:
    vc = input('você: ')
    vc_cnv = f'você: {vc}'
    vc_clean = (vc.translate(str.maketrans('', '', string.punctuation))).lower()
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
        monkey_cnv = f'MONKEY: {saudacao}, {novo_usuario.nome}, {saudacao_}! {frase}'
        salvar_cnv(vc_cnv, monkey_cnv)
        print(f'\n{monkey_cnv}\n')
        continue
    elif any(pergunta in vc_clean for pergunta in perguntas) and any(ser in vc_clean for ser in sers):
        termo = ' '.join(
            p for p in palavras if p not in perguntas and p not in sers and p not in artigos
        )
        monkey_cnv = buscar_api(termo)
        salvar_cnv(vc_cnv, monkey_cnv)
        print(f'\n{monkey_cnv}\n')
        continue
    elif any (palavrao in vc_clean for palavrao in palavroes):
        resposta = random.choice(resp_palavrao)
        monkey_c = f'MONKEY: {resposta}'
        salvar_cnv(vc_cnv, monkey_c)
        print(f'\n{monkey_c}\n')
        continue
    else:
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0 Safari/537.36'
        }
        response = requests.get('https://www.bing.com/search', params={'q': vc_no_monkey}, headers=headers)
        if response.status_code != 200:
            monkey_cnv = 'MONKEY: não consegui buscar isso agora.'
        else:
            soup = BeautifulSoup(response.text, 'html.parser')
            resultados = soup.find_all('li', class_='b_algo')
            primeiro = next((r for r in resultados if r.find('h2') and r.find('a')), None)
            if primeiro:
                titulo = primeiro.find('h2').get_text()
                link = primeiro.find('a')['href']
                monkey_cnv = f'MONKEY: {titulo} — {link}'
            else:
                monkey_cnv = 'MONKEY: não achei nada sobre isso.'
        salvar_cnv(vc_cnv, monkey_cnv)
        print(f'\n{monkey_cnv}\n')