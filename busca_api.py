from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def inicio():
    return {"mensagem": "Minha API está funcionando!"}


@app.get("/buscar")
def buscar(q: str):
    return {
        "consulta": q,
        "mensagem": "Pesquisa recebida!"
    }