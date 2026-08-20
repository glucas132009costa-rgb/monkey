from fastapi import FastAPI
import requests

app = FastAPI()

@app.get("/buscar")
def buscar(q: str):

    url = "https://pt.wikipedia.org/w/api.php"

    parametros = {
        "action": "query",
        "list": "search",
        "srsearch": q,
        "format": "json",
        "utf8": 1
    }

    try:
        resposta = requests.get(url, params=parametros)

        if resposta.status_code != 200:
            return {
                "consulta": q,
                "mensagem": "Erro ao acessar a Wikipédia."
            }

        dados = resposta.json()

        resultados = dados.get("query", {}).get("search", [])

        if not resultados:
            return {
                "consulta": q,
                "mensagem": "A Monkey não encontrou sua busca."
            }

        primeiro_resultado = resultados[0]

        titulo = primeiro_resultado["title"]

        # Agora pegamos o resumo da página encontrada
        url_resumo = "https://pt.wikipedia.org/api/rest_v1/page/summary/" + titulo.replace(" ", "_")

        resumo = requests.get(url_resumo)

        if resumo.status_code == 200:
            dados_resumo = resumo.json()

            return {
                "consulta": q,
                "mensagem": "A Monkey encontrou sua busca!",
                "titulo": dados_resumo.get("title", titulo),
                "resultado": dados_resumo.get(
                    "extract",
                    "Encontrei a página, mas não consegui obter o resumo."
                )
            }

        return {
            "consulta": q,
            "mensagem": "Encontrei a página, mas não consegui obter o resumo.",
            "resultado": titulo
        }

    except requests.exceptions.RequestException as erro:

        return {
            "consulta": q,
            "mensagem": "Erro de conexão com a Wikipédia.",
            "erro": str(erro)
        }