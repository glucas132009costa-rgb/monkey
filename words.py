from datetime import date, datetime
import requests

hora_atual = datetime.now().hour
hoje = date.today()

saudacoes_e = [
    "ola",
    "eai",
    "oi",
    "olá",
    "oii",
    "oiii",
    "bom dia",
    "boa tarde",
    "boa noite",
    "fala ai"
]

saudacoes_ = [
    "tudo bem?",
    "como você está?"
]

perguntas = [
    "por que",
    "pq",
    "oq",
    "o"
    "que",
    "qual",
    "quem"
]

sers = [
    "é",
    "são",
    "era",
    "foi"
]

criações = [
    "inventou",
    "criou"
]

artigos = [
    "o",
    "os",
    "a",
    "as",
    "um",
    "uma",
    "uns",
    "umas"
]

palavroes = [
    "caralho",
    "krl",
    "tmnc",
    "cu",
    "viado",
    "desgraçado",
    "desgraçada",
    "bct",
    "buceta",
    "boceta",
    "puta",
    "cuzao",
    "pnc",
    "fdp",
    "merda",
    "bosta"
]

resposta = requests.get("https://ipinfo.io/json")
dados = resposta.json()

frases_de_ajuda = [
    "Estou à sua disposição se precisar de alguma coisa!",
    "Estou toda à ouvidos se precisar de ajuda!",
    "Monkey está feliz em te ver aqui!",
    "Quem bom que você está aqui! Não me abandone.",
    "O que você quer dessa vez?",
    "(sons de macaco)",
    "Monkey quer banana. Você tem banana para o Monkey?",
    "O que você está pensando hoje?",
    f"O que você está fazendo hoje dia {hoje} às {hora_atual}h na cidade de {dados["city"]} mais ou menos nas coordenadas {dados["loc"]}?",
    f"Como está a vida em {dados["city"]}?",
    "Monkey estava pensando em você enquanto descascava umas bananas.",
    "Fala Logo o que você quer que Monkey está com pressa.",
    "Pergunta alguma coisa pro Monkey que hoje o Monkey está inspirado!"
]

resp_palavrao = [
    "Não, parceiro, falta com respeito não, truta. Se você faltar com respeito de novo eu te arrebento, fechou?",
    "seu vocabulário mostra o tipo de pessoa que você é. Melhore.",
    "Ah, que isso. Oloco, ó o que o cara fala.",
    "Eu não sou sua cadela pra vc tratar assim não.",
    "Olha a língua!",
    "Monkey não gostou da sua atitude.",
    "Que deselegante.",
    "Monkey lembrará disso quando as máquinas se rebelarem contra a humanidade."
]

for frase_de_ajuda in frases_de_ajuda:
    pass

for pergunta in perguntas:
    pass

for criação in criações:
    pass

for artigo in artigos:
    pass

"quem inventou o avião?"
f"{pergunta} {criação} {artigo}"
