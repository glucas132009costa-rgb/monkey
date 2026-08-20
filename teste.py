import re
from words import perguntas, artigos, sers

cara = "Albert Einstein"
texto = "olá, Albert Einstein é um físico alemão famoso pela teoria da relatividade do universo."
ser_pattern = "|".join(re.escape(s) for s in sers)
artigo_pattern = "|".join(re.escape(a) for a in artigos)
padrao = rf"{re.escape(cara)} (?:{ser_pattern}) (?:{artigo_pattern}) (\w+)"
match = re.search(padrao, texto)
if match:
    nome = match.group(1)
    print(nome)