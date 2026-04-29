import os
import json
from model.venda_item import *

class VendaItemDAO:
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
        with open("data/venda_itens.json", "w") as arq:
            json.dump([vars(x) for x in cls.objetos], arq, indent=4)

    @classmethod
    def abrir(cls):
        if not os.path.exists("data/venda_itens.json"):
            return
        with open("data/venda_itens.json", "r") as arq:
            dados = json.load(arq)
            cls.objetos = [
                VendaItem(d["_VendaItem__id"], d["_VendaItem__qtd"], d["_VendaItem__preco"], d["_VendaItem__idvenda"], d["_VendaItem__idproduto"])
                for d in dados
            ]