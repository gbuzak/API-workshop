from fastapi import FastAPI
from typing import List, Dict

app = FastAPI()

produtos: List[Dict[str,any]] = [
    {
        "id": 1,
        "nome": "Smartphone",
        "descricao": "Um smartphone top de linha",
        "preco": 1500.0
    },
    {
        "id": 2,
        "nome": "Notebook",
        "descricao": "Um notebook gamer",
        "preco": 3500.0
    },
    {
        "id": 3,
        "nome": "Tablet",
        "descricao": "Um tablet para estudos",
        "preco": 2500.0
    }
]


@app.get("/") # Request
def ola_mundo(): # Response
    return {"Olá": "Mundo2"}


@app.get("/produtos") # Request
def listar_produtos():
    return produtos


