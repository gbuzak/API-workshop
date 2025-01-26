from typing import List, Dict

class Produtos:
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

    def listar_produtos(self):
        return self.produtos

    def buscar_produtos(self, id):
        for produto in self.produtos:
            if produto["id"] == id:
                return produto
        return {"Status":404, "Mensagem": "Produto não encontrado"}
    
    def adicionar_produtos(self, produto):
        self.produtos.append(produto)
        return produto