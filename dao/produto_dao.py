import os
import json
from model.produto import *

class ProdutoDAO:
    objetos = []

    @classmethod
    def inserir(cls, obj):
        cls.objetos.append(obj)
        cls.salvar()

    @classmethod
    def listar(cls):
        return cls.objetos

    @classmethod
    def listar_id(cls, id):
        for x in cls.objetos:
            if x.get_id() == id:
                return x
        return None

    @classmethod
    def atualizar(cls, obj):
        for i in range(len(cls.objetos)):
            if cls.objetos[i].get_id() == obj.get_id():
                cls.objetos[i] = obj
                cls.salvar()
                return True
        return False

    @classmethod
    def excluir(cls, id):
        for i in range(len(cls.objetos)):
            if cls.objetos[i].get_id() == id:
                del cls.objetos[i]
                cls.salvar()
                return True
        return False

    @classmethod
    def salvar(cls):
        with open("data/produtos.json", "w") as arq:
            json.dump([vars(x) for x in cls.objetos], arq, indent=4)

    @classmethod
    def abrir(cls):
        if not os.path.exists("data/produtos.json"):
            return
        with open("data/produtos.json", "r") as arq:
            dados = json.load(arq)
            cls.objetos = [
                Produto(d["_Produto__id"], d["_Produto__descricao"], d["_Produto__preco"], d["_Produto__estoque"], d["_Produto__idcategoria"])
                for d in dados
            ]