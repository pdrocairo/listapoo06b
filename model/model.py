import os
import json
from datetime import datetime

class Cliente:
    def __init__(self, id, nome, email, fone):
        self.__id = int(id)
        self.__nome = nome
        self.__email = email
        self.__fone = fone

    def set_nome(self, nome): 
        self.__nome = nome
    def set_fone(self, fone):
        self.__fone = fone
    def set_email(self, email):
        self.__email = email

    def get_id(self):
        return self.__id
    def get_nome(self):
        return self.__nome
    def get_fone(self):
        return self.__fone
    def get_email(self):
        return self.__email    

    def ToString(self):
        return f"ID: {self.__id} | Nome: {self.__nome} | Fone: {self.__fone}"

class Venda:
    def __init__(self, id, data, carrinho, total, idCliente):
        self.__id = int(id)
        self.__data = data
        self.__carrinho = bool(carrinho)
        self.__total = total
        self.__idCliente = idCliente

    def get_id(self):
        return self.__id
    def get_data(self):
        return self.__data
    def get_carrinho(self):
        return self.__carrinho
    def get_total(self):
        return self.__total
    def get_idCliente(self):
        return self.__idCliente

    def set_data(self, data):
        self.__data = data
    def set_carrinho(self, status):
        self.__carrinho = bool(status)
    def set_total(self, total):
        self.__total = total
    def set_idCliente(self, idcliente):
        self.__idCliente = idcliente

    def ToString(self):
        status = "Aberto" if self.__carrinho else "Finalizado"
        return f"VENDA: {self.__id} [{status}] | Cliente: {self.__idCliente} | Total: R${self.__total}"

class VendaItem:
    def __init__(self, id, qtd, preco, idvenda, idproduto):
        self.__id = int(id)
        self.__qtd = qtd
        self.__preco = preco
        self.__idvenda = idvenda
        self.__idproduto = idproduto

    def set_qtd(self, qtd):
        self.__qtd = qtd
    def set_preco(self, preco):
        self.__preco = preco
    def set_idvenda(self, idvenda):
        self.__idvenda = idvenda
    def set_idproduto(self, idproduto):
        self.__idproduto = idproduto

    def get_id(self):
        return self.__id
    def get_qtd(self):
        return self.__qtd
    def get_preco(self):
        return self.__preco
    def get_idvenda(self):
        return self.__idvenda
    def get_idproduto(self):
        return self.__idproduto

    def ToString(self):
        return f"   -> Item: {self.__id} | Prod: {self.__idproduto} | Qtd: {self.__qtd} | Preço Un: {self.__preco}"
    
class Produto:
    def __init__(self, id, descricao, preco, estoque, idcategoria):
        self.__id = int(id)
        self.__descricao = descricao
        self.__preco = preco
        self.__estoque = estoque
        self.__idcategoria = idcategoria

    def set_descricao(self, descricao):
        self.__descricao = descricao
    def set_preco(self, preco):
        self.__preco = preco
    def set_estoque(self, estoque):
        self.__estoque = estoque
    def set_idcategoria(self, idcategoria):
        self.__idcategoria = idcategoria

    def get_id(self):
        return self.__id
    def get_descricao(self):
        return self.__descricao
    def get_preco(self):
        return self.__preco
    def get_estoque(self):
        return self.__estoque
    def get_idcategoria(self):
        return self.__idcategoria

    def ToString(self):
        return f"ID: {self.__id} | {self.__descricao} | Preço: {self.__preco} | Cat: {self.__idcategoria}"
    
class Categoria:
    def __init__(self, id, categoria):
        self.__id = int(id)
        self.__categoria = categoria

    def set_categoria(self, categoria):
        self.__categoria = categoria

    def get_id(self):
        return self.__id
    def get_categoria(self):
        return self.__categoria
    
    def ToString(self):
        return f"ID: {self.__id} | Categoria: {self.__categoria}"