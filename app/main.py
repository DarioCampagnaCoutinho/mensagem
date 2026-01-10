from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def read_root():
    """Rota raiz que retorna uma mensagem simples em JSON."""
    return {"message": "Olá, mundo!"}

