from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"status": "API online 🚀"}


@app.get("/usuario/{nome}")
def usuario(nome: str):
    return {"msn": f"Ola {nome}"}