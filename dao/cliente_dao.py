import os
import json
from datetime import datetime
from model.cliente import *

class ClienteDAO:
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
            if x.get_id() == id: return x
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
        with open("data/clientes.json", "w") as arq:
            json.dump([vars(x) for x in cls.objetos], arq, indent=4)
    
    @classmethod
    def abrir(cls):
        if not os.path.exists("data/clientes.json"): return
        with open("data/clientes.json", "r") as arq:
            dados = json.load(arq)
            cls.objetos = [Cliente(d['_Cliente__id'], d['_Cliente__nome'], d['_Cliente__email'], d['_Cliente__fone']) for d in dados]