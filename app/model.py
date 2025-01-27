from sqlalchemy import Column, Integer, String, Float
from sqlalchemy.orm import declarative_base

base = declarative_base()

class Produto(base):
    __tablename__ = 'produtos'
    id = Column(Integer, primary_key=True, index=True)
    titulo = Column(String, nullable=False)
    descricao = Column(String)
    preco = Column(Float, nullable=False)