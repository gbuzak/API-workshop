from fastapi import FastAPI
from .schema import ProdutosSchema
from .data import Produtos
from typing import List

app = FastAPI()
lista_de_produtos = Produtos()


@app.get("/") # Request
def ola_mundo(): # Response
    return {"Olá": "Mundo"}


@app.get("/produtos", response_model=List[ProdutosSchema]) # Request
def listar_produtos():
    return lista_de_produtos.listar_produtos()


@app.get("/produtos/{id}", response_model=ProdutosSchema) # Request
def buscar_produtos(id: int):
    return lista_de_produtos.buscar_produtos(id)

@app.post("/produtos", response_model=ProdutosSchema) # Request
def adicionar_produtos(produto: ProdutosSchema):
    return lista_de_produtos.adicionar_produtos(produto)