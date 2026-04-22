import os
from datetime import datetime


class Cliente:
    def __init__(self, nome, telefone, email, id):
        self.__nome = nome
        self.__telefone = telefone
        self.__email = email
        self.__id = id
        
    def set_id(self, id):
        self.__id = id

    def get_id(self):
        return self.__id

    def set_nome(self, nome):
        self.__nome = nome

    def get_nome(self):
        return self.__nome
    
    def set_telefone(self, telefone):
        self.__telefone = telefone

    def get_telefone(self):
        return self.__telefone

    def set_email(self, email):
        self.__email = email

    def get_email(self):
        return self.__email

    def ToString(self):
        return f"ID: {self.get_id()}, NOME: {self.get_nome()}, TELEFONE: {self.get_telefone()}, EMAIL: {self.get_email()}"

class Venda:
    def __init__(self, id, data, carrinho, total):
        self.__id = id
        self.__data = data
        self.__total = total
        self.__carrinho = carrinho
    
    def set_idvenda(self, id):
        self.__id = id

    def set_data(self, data):
        self.__data = data

    def set_carrinho(self, carrinho):
        self.__carrinho = carrinho

    def set_total(self, total):
        self.__total = total

    def get_id(self):
        return self.__id
    
    def get_data(self):
        return self.__data
    
    def get_carrinho(self):
        return self.__carrinho
    
    def get_total(self):
        return self.__total
    
    def ToString(self):
        return f"ID DA VENDA: {self.get_idvenda()}, DATA: {self.get_data()}, CARRINHO: {self.get_carrinho()}, TOTAL: {self.set_total()}"

class VendaItem:
    def __init__(self, id, qtd, preco, idvenda, idproduto):
        self.__id = id
        self.__qtd = qtd
        self.__preco = preco
        self.__idvenda = idvenda
        self.__idproduto = idproduto

    def set_id(self, id):
        self.__id = id
    
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
        return f"ID: {self.get_id()}, QUANTIDADE: {self.get_qtd()}, PREÇO: {self.get_preco()}, ID DA VENDA: {self.get_idvenda()}, ID DO PRODUTO: {self.get_idproduto()}"

class Produto:
    def __init__(self, id, descricao, preco, estoque, idcategoria):
        self.__id = id
        self.__descricao = descricao
        self.__preco = preco
        self.__estoque = estoque
        self.__idcategoria = idcategoria

    def set_id(self, id):
        self.__id = id

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
        return f"ID: {self.get_id()}, DESCRIÇAO: {self.get_descricao()}, PREÇO: {self.get_preco()}, ESTOQUE: , ID DA CATEGORIA: {self.get_idcategoria()}"
    
class Categoria:
    def __init__(self, id, categoria):
        self.__id = id
        self.__categoria = categoria

    def set_id(self, id):
        self.__id = id

    def set_categoria(self, categoria):
        self.__categoria = categoria

    def get_id(self):
        return self.__id
        
    def get_categoria(self):
        return self.__categoria
    
    def ToString(self):
        return f"ID: {self.get_id()}, CATEGORIA: {self.get_categoria()}"
    
class ClienteDAO:
    def __init__(self):
        self.__listaclientes = []

    def adicionar_clientes(self, cliente):
        if isinstance(cliente, Cliente):
            self.__listaclientes.append(cliente)

    def mostrar_clientes(self):
        return self.__listaclientes
    
    def mostrar_clientesID(self):
        lista = []
        if len(self.__listaclientes) > 0:
            for cliente in self.__listaclientes:
                lista.append(cliente.get_id())
            return lista
        else:
            return "Lista Vazia"
    
    def excluir_cliente(self):
        if len(self.__listaclientes) > 0:
            id = input("Digite o ID do usuário que vc quer excluir: ")
            for cliente in self.__listaclientes:
                if id == cliente.get_id():
                    self.__listaclientes.remove(cliente)
                    print("Cliente removido com sucesso!")
                    break
        else:
            return "Nao tem IDS NA LISTA"
    
    def atualizar_cliente(self):
        if len(self.__listaclientes) > 0:
            for cliente in self.mostrar_clientes():
                print(cliente.ToString())
            id = input("Digite o ID do usuário que vc quer atualizar: ")
            for cliente in self.__listaclientes:
                if id == cliente.get_id():
                    nome = input("Digite um novo nome para o cliente: ")
                    cliente.set_nome(nome)
                    telefone = input("Digite um novo telefone para o cliente: ")
                    cliente.set_telefone(telefone)
                    email = input("Digite um novo email para o cliente: ")
                    cliente.set_email(email)
                    print("\nCliente atualizado com sucesso!")
                    print(cliente.ToString())
                    break
            else:
                print("\nCLIENTE NÃO ENCONTRADO\n")
        else:
            print("\nNENHUM CLIENTE CADASTRADO\n")
                    
class VendaDAO:
    def __init__(self):
        self.listavendas = []

    def adicionar_venda(self, venda):
        if isinstance(venda, Venda):
            self.listavendas.append(venda)
        else:
            print("\nNENHUM VENDA CADASTRADO\n")

    def mostrar_vendas(self):
        if len(self.listavendas) > 0:
            return self.listavendas
        else:
            return "Lista Vazia"
    def mostrar_vendasID(self):
        lista = []
        if len(self.listavendas) > 0:
            for venda in self.listavendas:
                lista.append(venda.get_id())
            return lista
        else:
            return "Lista Vazia"

    def excluir_venda(self):
        if len(self.listavendas) > 0:
            for venda in self.listavendas:
                print(venda.ToString())
            id = input("Digite o ID do venda que vc quer excluir: ")
            for venda in self.listavendas:
                if id == venda.get_id():
                    self.listavendas.remove(venda)
                    print("Venda removida com sucesso!")
                    break
                else:
                    print("Nao tem vendas com este ID")

    def atualizar_venda(self):
        if len(self.listavendas) > 0:
            for venda in self.listavendas:
                print(venda.ToString())
            id = input("Digite o ID do venda que vc quer atualizar: ")
            for venda in self.listavendas:
                if id == venda.get_id():
                    # data, carrinho, total
                    data = input("Digite o data do venda que vc quer atualizar: ")
                    venda.set_data(data)
                    carrinho = input("Digite os itens do seu carrinho: ")
                    venda.set_carrinho(carrinho)
                    total = input("Digite o total do venda a ser atualizada: ")
                    venda.set_total(total)
                else:
                    print("Nao tem vendas com este ID")

        else:
            print("\nNENHUM VENDA CADASTRADO\n")

class VendaItemDAO:
    def __init__(self):
        self.listavendaItem = []

    def adicionar_venda(self, venda):
        if isinstance(venda, Venda):
            self.listavendaItem.append(venda)
        else:
            print("\nNAO EH UMA VENDA VALIDA\n")

    def mostrar_vendas(self):
        if len(self.listavendaItem) > 0:
            return self.listavendaItem
        else:
            return "Lista Vazia"

    def mostrar_vendasID(self):
        lista = []
        if len(self.listavendaItem) > 0:
            for venda in self.listavendaItem:
                lista.append(venda.get_id())
            return lista
        else:
            return "Lista Vazia"

    def excluir_venda(self):
        if len(self.listavendaItem) > 0:
            for venda in self.listavendaItem:
                print(venda.ToString())
            id = input("Digite o ID do item da venda que vc quer excluir: ")
            for venda in self.listavendaItem:
                if id == venda.get_idvenda():
                    self.listavendaItem.remove(venda)
                else:
                    print("Nao tem vendas com este ID")

        else:
            print("\nNENHUM id ITEM VENDA CADASTRADO\n")

    def atualizar_venda(self):
        if len(self.listavendaItem) > 0:
            for venda in self.listavendaItem:
                print(venda.ToString())
            id = input("Digite o ID do item da venda que vc quer atualizar: ")
            for venda in self.listavendaItem:
                if id == venda.get_idvenda():
                    qtd = input("Digite o qtd do item da venda que vc quer atualizar: ")
                    venda.set_qtd(qtd)
                    preco = input("Digite o preco do item da venda que vc quer atualizar: ")
                    venda.set_preco(preco)
                    idproduto = input("Digite o id do produto que vc quer atualizar: ")
                    venda.set_idproduto(idproduto)
        else:
            print("\nNENHUM ITEM VENDA CADASTRADO\n")








                    # id, qtd, preco, idvenda, idproduto








# cliente = Cliente("pedro", "8491-1191", "pedro.cairo@mail.com", "1")
#
# dao = ClienteDAO()
# dao.adicionar_clientes(cliente)
# clientes = dao.mostrar_clientesID()
#
#
#
# # for c in clientes:
# #     print(c.ToString())