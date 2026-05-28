from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"status": "API online 🚀"}


@app.get("/usuario/{nome}")
def usuario(nome: str):
    return {"msn": f"Ola {nome}"}


@app.get("/authenticate/{id}")
def auth(id: str):

    __list_authentic = [
        {
            "key": "1234",
            "status": "ativado"
        },
        {
            "key": "uni_micro_centro",
            "status": "ativado"
        },
        {
            "key": "uni_micro_cidade_nova",
            "status": "desativado"
        }
    ]

    for item in __list_authentic:
        if item.get("key") == id:
            return item
