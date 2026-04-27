import os
import json
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
    def __init__(self, id, data, carrinho, total, idCliente):
        self.__id = id
        self.__data = data
        self.__total = total
        self.__carrinho = carrinho
        self.__idCliente = idCliente
    
    def set_idvenda(self, id):
        self.__id = id

    def set_data(self, data):
        self.__data = data

    def set_carrinho(self, carrinho):
        self.__carrinho = carrinho

    def set_total(self, total):
        self.__total = total
        
    def set_idCliente(self, idCliente):
        self.__idCliente = idCliente

    def get_idCliente(self):
        return self.__idCliente

    def get_id(self):
        return self.__id
    
    def get_data(self):
        return self.__data
    
    def get_carrinho(self):
        return self.__carrinho
    
    def get_total(self):
        return self.__total
    
    def ToString(self):
        return f"ID DA VENDA: {self.get_id()}, ID DO CLIENTE: {self.get_idCliente()}, DATA: {self.get_data()}, CARRINHO: {self.get_carrinho()}, TOTAL: {self.get_total()}"

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
        return f"ID: {self.get_id()}, DESCRIÇAO: {self.get_descricao()}, PREÇO: {self.get_preco()}, ESTOQUE: {self.get_estoque()}, ID DA CATEGORIA: {self.get_idcategoria()}"
    
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

    def salvar_arquivo(self):
        dados = []
        for cliente in self.__listaclientes:
            dados.append(
                {
                    "id": cliente.get_id(),
                    "nome": cliente.get_nome(),
                    "telefone": cliente.get_telefone(),
                    "email": cliente.get_email(),
                }
            )

        with open("clientes.json", "w", encoding="utf-8") as arquivo:
            json.dump(dados, arquivo, ensure_ascii=False, indent=4)

    def carregar_arquivo(self):
        if not os.path.exists("clientes.json"):
            return

        with open("clientes.json", "r", encoding="utf-8") as arquivo:
            dados = json.load(arquivo)

        self.__listaclientes = []
        for item in dados:
            cliente = Cliente(item["nome"], item["telefone"], item["email"], item["id"])
            self.__listaclientes.append(cliente)

    def adicionar_clientes(self, cliente):
        if isinstance(cliente, Cliente):
            self.__listaclientes.append(cliente)
            self.salvar_arquivo()

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
                    self.salvar_arquivo()
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
                    self.salvar_arquivo()
                    break
            else:
                print("\nCLIENTE NÃO ENCONTRADO\n")
        else:
            print("\nNENHUM CLIENTE CADASTRADO\n")
                    
class VendaDAO:
    def __init__(self):
        self.listavendas = []

    def salvar_arquivo(self):
        dados = []
        for venda in self.listavendas:
            dados.append(
                {
                    "id": venda.get_id(),
                    "idCliente": venda.get_idCliente(),
                    "data": venda.get_data(),
                    "carrinho": venda.get_carrinho(),
                    "total": venda.get_total(),
                }
            )

        with open("vendas.json", "w", encoding="utf-8") as arquivo:
            json.dump(dados, arquivo, ensure_ascii=False, indent=4)

    def carregar_arquivo(self):
        if not os.path.exists("vendas.json"):
            return

        with open("vendas.json", "r", encoding="utf-8") as arquivo:
            dados = json.load(arquivo)

        self.listavendas = []
        for item in dados:
            id_cliente = item.get("idCliente", "Desconhecido")
            venda = Venda(item["id"], item["data"], item["carrinho"], item["total"], id_cliente)
            self.listavendas.append(venda)

    def adicionar_venda(self, venda):
        if isinstance(venda, Venda):
            self.listavendas.append(venda)
            self.salvar_arquivo()
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
                    self.salvar_arquivo()
                    break
                else:
                    print("Nao tem vendas com este ID")

    def atualizar_venda(self):
        if len(self.listavendas) > 0:
            for venda in self.listavendas:
                print(venda.ToString())
            id = input("Digite o ID da venda que vc quer atualizar: ")
            for venda in self.listavendas:
                if id == venda.get_id():
                    data = input("Digite a data da venda que vc quer atualizar: ")
                    venda.set_data(data)
                    
                    id_cliente = input("Digite o novo ID do cliente: ")
                    venda.set_idCliente(id_cliente)
                    
                    carrinho = input("Digite os itens do seu carrinho: ")
                    venda.set_carrinho(carrinho)
                    total = input("Digite o total da venda a ser atualizada: ")
                    venda.set_total(total)
                    self.salvar_arquivo()
                    print("Venda atualizada com sucesso!")
                    break
            else:
                print("Nao tem vendas com este ID")
        else:
            print("\nNENHUMA VENDA CADASTRADA\n")

class VendaItemDAO:
    def __init__(self):
        self.listavendaItem = []

    def salvar_arquivo(self):
        dados = []
        for item in self.listavendaItem:
            dados.append(
                {
                    "id": item.get_id(),
                    "qtd": item.get_qtd(),
                    "preco": item.get_preco(),
                    "idvenda": item.get_idvenda(),
                    "idproduto": item.get_idproduto(),
                }
            )

        with open("venda_itens.json", "w", encoding="utf-8") as arquivo:
            json.dump(dados, arquivo, ensure_ascii=False, indent=4)

    def carregar_arquivo(self):
        if not os.path.exists("venda_itens.json"):
            return

        with open("venda_itens.json", "r", encoding="utf-8") as arquivo:
            dados = json.load(arquivo)

        self.listavendaItem = []
        for item in dados:
            venda_item = VendaItem(item["id"], item["qtd"], item["preco"], item["idvenda"], item["idproduto"])
            self.listavendaItem.append(venda_item)

    def adicionar_venda(self, venda):
        if isinstance(venda, VendaItem):
            self.listavendaItem.append(venda)
            self.salvar_arquivo()
        else:
            print("NAO EH UM ITEM DE VENDA VALIDO")

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
                    self.salvar_arquivo()
                else:
                    raise ValueError("Nao tem vendas com este ID")

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
                    self.salvar_arquivo()
        else:
            print("\nNENHUM ITEM VENDA CADASTRADO\n")

class ProdutoDao:
    def __init__(self):
        self.__listaproduto = []

    def salvar_arquivo(self):
        dados = []
        for produto in self.__listaproduto:
            dados.append(
                {
                    "id": produto.get_id(),
                    "descricao": produto.get_descricao(),
                    "preco": produto.get_preco(),
                    "estoque": produto.get_estoque(),
                    "idcategoria": produto.get_idcategoria(),
                }
            )

        with open("produtos.json", "w", encoding="utf-8") as arquivo:
            json.dump(dados, arquivo, ensure_ascii=False, indent=4)

    def carregar_arquivo(self):
        if not os.path.exists("produtos.json"):
            return

        with open("produtos.json", "r", encoding="utf-8") as arquivo:
            dados = json.load(arquivo)

        self.__listaproduto = []
        for item in dados:
            produto = Produto(item["id"], item["descricao"], item["preco"], item["estoque"], item["idcategoria"])
            self.__listaproduto.append(produto)

    def adicionar_produto(self, produto):
        if isinstance(produto, Produto):
            self.__listaproduto.append(produto)
            self.salvar_arquivo()
        else:
            raise ValueError("Não é um produto válido")
        
    def mostrar_produtos(self):
        lista = []
        if len(self.__listaproduto) > 0:
            for produto in self.__listaproduto:
                lista.append(produto.ToString())
            return lista
        else:
            raise ValueError("Não tem produtos na lista")
        
    def mostrar_produtosID(self):
        lista = []
        if len(self.__listaproduto) > 0:
            for produto in self.__listaproduto:
                lista.append(produto.get_id())
            return lista
        else:
            raise ValueError("Não tem produtos na lista")
        
    def excluir_produto(self):
        if len(self.__listaproduto) > 0:
            id = input("Digite o ID para excluir o produto: ")
            for produto in self.__listaproduto:
                if id == produto.get_id():
                    self.__listaproduto.remove(produto)
                    self.salvar_arquivo()
                    break
                else:
                    print("Nenhum produto encontrado com esse ID")
        else:
            raise ValueError("A lista não tem produtos")
        
    def atualizar_produto(self):
        if len(self.__listaproduto) > 0:
            id = input("Digite o ID do produto que voce quer atualizar: ")
            for produto in self.__listaproduto:
                if id == produto.get_id():
                    descricao = input("Digite a descricao nova: ")
                    produto.set_descricao(descricao)
                    preco = input("Digite o novo preco: ")
                    produto.set_preco(preco)
                    estoque = input("Digite o novo estoque: ")
                    produto.set_estoque(estoque)
                    idcategoria = input("Digite o novo ID da categoria: ")
                    produto.set_idcategoria(idcategoria)
                    self.salvar_arquivo()
                    break
                else:
                    print("Nenhum produto encontrado com esse ID")
        else:
            raise ValueError("A lista não tem produtos")

class CategoriaDAO:
    def __init__(self):
        self.__listacategoria = []

    def salvar_arquivo(self):
        dados = []
        for categoria in self.__listacategoria:
            dados.append(
                {
                    "id": categoria.get_id(),
                    "categoria": categoria.get_categoria(),
                }
            )

        with open("categorias.json", "w", encoding="utf-8") as arquivo:
            json.dump(dados, arquivo, ensure_ascii=False, indent=4)

    def carregar_arquivo(self):
        if not os.path.exists("categorias.json"):
            return

        with open("categorias.json", "r", encoding="utf-8") as arquivo:
            dados = json.load(arquivo)

        self.__listacategoria = []
        for item in dados:
            categoria = Categoria(item["id"], item["categoria"])
            self.__listacategoria.append(categoria)

    def adicionar_categoria(self, categoria):
        if isinstance(categoria, Categoria):
            self.__listacategoria.append(categoria)
            self.salvar_arquivo()
        else:
            raise ValueError("Não é uma categoria válida")
    
    def mostrar_categoria(self):
        lista = []
        if len(self.__listacategoria) > 0:
            for categoria in self.__listacategoria:
                lista.append(categoria.ToString())
            return lista
        else:
            raise ValueError("Não tem categorias na lista")

    def mostrar_categoriaID(self):
        lista = []
        if len(self.__listacategoria) > 0:
            for categoria in self.__listacategoria:
                lista.append(categoria.get_id())
            return lista
        else:
            raise ValueError("Não tem categoria na lista")

    def excluir_categoria(self):
        if len(self.__listacategoria) > 0:
            id = input("Digite o ID para excluir a categoria: ")
            for categoria in self.__listacategoria:
                if id == categoria.get_id():
                    self.__listacategoria.remove(categoria)
                    self.salvar_arquivo()
                    break
                else:
                    print("Nenhuma categoria encontrada com esse ID")
        else:
            raise ValueError("A lista não tem categorias")

    def atualizar_categoria(self):
        if len(self.__listacategoria) > 0:
            id = input("Digite o ID do produto que voce quer atualizar: ")
            for categoria in self.__listacategoria:
                if id == categoria.get_id():
                    categoria.set_categoria(categoria)
                    self.salvar_arquivo()
                    break
                else:
                    print("Nenhuma categoria encontrado com esse ID")
        else:
            raise ValueError("A lista não tem categoria")


class UI:
    def __init__(self):
        self.cliente_dao = ClienteDAO()
        self.venda_dao = VendaDAO()
        self.vendaitem_dao = VendaItemDAO()
        self.produto_dao = ProdutoDao()
        self.categoria_dao = CategoriaDAO()
        self.carregar_todos_arquivos()
        self.salvar_todos_arquivos()

    def carregar_todos_arquivos(self):
        self.cliente_dao.carregar_arquivo()
        self.venda_dao.carregar_arquivo()
        self.vendaitem_dao.carregar_arquivo()
        self.produto_dao.carregar_arquivo()
        self.categoria_dao.carregar_arquivo()

    def salvar_todos_arquivos(self):
        self.cliente_dao.salvar_arquivo()
        self.venda_dao.salvar_arquivo()
        self.vendaitem_dao.salvar_arquivo()
        self.produto_dao.salvar_arquivo()
        self.categoria_dao.salvar_arquivo()

    def menu(self):
        print("----------------------------")
        print("1. CRUD Clientes")
        print("2. CRUD Venda")
        print("3. CRUD VendaItem")
        print("4. CRUD Produtos")
        print("5. CRUD Categoria")
        print("6. Sair")
        print("----------------------------\n")
        return input("Escolha uma opção: ")
    
    def menu_cliente(self):
        print("1 - Criar Cliente")
        print("2 - Listar Cliente")
        print("3 - Atualizar Cliente")
        print("4 - Excluir Clientes")
        print("5 - Sair")
        return input("Digite o número da opçao: ")
    
    def menu_venda(self):
        print("1 - Criar Venda")
        print("2 - Listar Venda")
        print("3 - Atualizar Venda")
        print("4 - Excluir Vendas")
        print("5 - Sair")
        return input("Digite o número da opçao: ")
    
    def menu_vendaitem(self):
        print("1 - Criar Item pra Venda")
        print("2 - Listar Itens pra Venda")
        print("3 - Atualizar Itens pra Venda")
        print("4 - Excluir Itens pra Vendas")
        print("5 - Sair")
        return input("Digite o número da opçao: ")

    def menu_produto(self):
        print("1 - Criar Produto")
        print("2 - Listar Produto")
        print("3 - Atualizar Produto")
        print("4 - Excluir Produtos")
        print("5 - Sair")
        return input("Digite o número da opçao: ")
    
    def menu_categoria(self):
        print("1 - Criar Categoria")
        print("2 - Listar Categoria")
        print("3 - Atualizar Categoria")
        print("4 - Excluir Categorias")
        print("5 - Sair")
        return input("Digite o número da opçao: ")
    
    def main(self):
        while True:
            opcao = self.menu()
            if opcao == '1':
                self.executar_menu_cliente()
            elif opcao == '2':
                self.executar_menu_venda()
            elif opcao == '3':
                self.executar_menu_vendaitem()
            elif opcao == '4':
                self.executar_menu_produto()
            elif opcao == '5':
                self.executar_menu_categoria()
            elif opcao == '6':
                self.salvar_todos_arquivos()
                print("Encerrando sistema...")
                break
            else:
                print("Opção inválida.")

    def executar_menu_cliente(self):
        while True:
            opcao = self.menu_cliente()
            if opcao == '1':
                self.criar_cliente()
            elif opcao == '2':
                self.mostrar_cliente()
            elif opcao == '3':
                self.atualizar_cliente()
            elif opcao == '4':
                self.excluir_cliente()
            elif opcao == '5':
                break
            else:
                print("Opção inválida.")

    def executar_menu_venda(self):
        while True:
            opcao = self.menu_venda()
            if opcao == '1':
                self.criar_venda()
            elif opcao == '2':
                self.mostrar_vendas()
            elif opcao == '3':
                self.venda_dao.atualizar_venda()
            elif opcao == '4':
                self.venda_dao.excluir_venda()
            elif opcao == '5':
                break
            else:
                print("Opção inválida.")

    def executar_menu_vendaitem(self):
        while True:
            opcao = self.menu_vendaitem()
            if opcao == '1':
                self.criar_item_venda()
            elif opcao == '2':
                self.mostrar_itens_venda()
            elif opcao == '3':
                self.vendaitem_dao.atualizar_venda()
            elif opcao == '4':
                self.vendaitem_dao.excluir_venda()
            elif opcao == '5':
                break
            else:
                print("Opção inválida.")

    def executar_menu_produto(self):
        while True:
            opcao = self.menu_produto()
            if opcao == '1':
                self.criar_produto()
            elif opcao == '2':
                self.mostrar_produtos()
            elif opcao == '3':
                self.produto_dao.atualizar_produto()
            elif opcao == '4':
                self.produto_dao.excluir_produto()
            elif opcao == '5':
                break
            else:
                print("Opção inválida.")

    def executar_menu_categoria(self):
        while True:
            opcao = self.menu_categoria()
            if opcao == '1':
                self.criar_categoria()
            elif opcao == '2':
                self.mostrar_categorias()
            elif opcao == '3':
                self.categoria_dao.atualizar_categoria()
            elif opcao == '4':
                self.categoria_dao.excluir_categoria()
            elif opcao == '5':
                break
            else:
                print("Opção inválida.")

    def criar_cliente(self):
        id = input("Digite um ID pro cliente: ")
        nome = input("Digite um nome pro cliente: ")
        email = input("Digite um email pro cliente: ")
        telefone = input("Digite um telefone pro cliente: ")

        cliente = Cliente(nome, telefone, email, id)
        self.cliente_dao.adicionar_clientes(cliente)

    def mostrar_cliente(self):
        clientes = self.cliente_dao.mostrar_clientes()
        if len(clientes) == 0:
            print("Nenhum cliente cadastrado.")
            return

        for cliente in clientes:
            print(cliente.ToString())

    def mostrar_clienteID(self):
        self.cliente_dao.mostrar_clientesID()

    def atualizar_cliente(self):
        self.cliente_dao.atualizar_cliente()

    def excluir_cliente(self):
        self.cliente_dao.excluir_cliente()

    def criar_venda(self):
        id = input("Digite um ID pra venda: ")
        id_cliente = input("Digite o ID do cliente que está fazendo a compra: ")
        data = input("Digite a data da venda (dd/mm/aaaa): ")
        carrinho = input("Digite os itens do carrinho: ")
        total = input("Digite o total da venda: ")

        venda = Venda(id, data, carrinho, total, id_cliente)
        self.venda_dao.adicionar_venda(venda)
        print("Venda cadastrada com sucesso!")

    def mostrar_vendas(self):
        vendas = self.venda_dao.mostrar_vendas()
        if isinstance(vendas, str):
            print(vendas)
            return

        for venda in vendas:
            print(venda.ToString())

    def criar_item_venda(self):
        id = input("Digite um ID pro item da venda: ")
        qtd = input("Digite a quantidade: ")
        preco = input("Digite o preço: ")
        idvenda = input("Digite o ID da venda: ")
        idproduto = input("Digite o ID do produto: ")

        item = VendaItem(id, qtd, preco, idvenda, idproduto)
        self.vendaitem_dao.adicionar_venda(item)

    def mostrar_itens_venda(self):
        itens = self.vendaitem_dao.mostrar_vendas()
        if isinstance(itens, str):
            print(itens)
            return

        for item in itens:
            print(item.ToString())

    def criar_produto(self):
        id = input("Digite um ID pro produto: ")
        descricao = input("Digite a descrição do produto: ")
        preco = input("Digite o preço do produto: ")
        estoque = input("Digite o estoque do produto: ")
        idcategoria = input("Digite o ID da categoria: ")

        produto = Produto(id, descricao, preco, estoque, idcategoria)
        self.produto_dao.adicionar_produto(produto)

    def mostrar_produtos(self):
        try:
            produtos = self.produto_dao.mostrar_produtos()
            for produto in produtos:
                print(produto)
        except ValueError as erro:
            print(erro)

    def criar_categoria(self):
        id = input("Digite um ID pra categoria: ")
        nome_categoria = input("Digite o nome da categoria: ")

        categoria = Categoria(id, nome_categoria)
        self.categoria_dao.adicionar_categoria(categoria)

    def mostrar_categorias(self):
        try:
            categorias = self.categoria_dao.mostrar_categoria()
            for categoria in categorias:
                print(categoria)
        except ValueError as erro:
            print(erro)

if __name__ == "__main__":
    UI().main()





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