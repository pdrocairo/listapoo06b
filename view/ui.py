from model.venda_item import *
from dao.venda_item_dao import *

from model.venda import *
from dao.venda_dao import *

from model.produto import *
from dao.produto_dao import *

from model.categoria import *
from dao.categoria_dao import *

from model.cliente import *
from dao.cliente_dao import *







class UI:
    @staticmethod
    def main():
        ClienteDAO.abrir()
        CategoriaDAO.abrir()
        ProdutoDAO.abrir()
        VendaDAO.abrir()
        VendaItemDAO.abrir()

        while True:
            op = UI.menu_principal()
            if op == "0":
                break
            elif op == "1":
                UI.menu_clientes()
            elif op == "2":
                UI.menu_vendas()
            elif op == "3":
                UI.menu_venda_itens()
            elif op == "4":
                UI.menu_produtos()
            elif op == "5":
                UI.menu_categorias()

    @staticmethod
    def menu_principal():
        print("\n--- SISTEMA CRUD ---")
        print("1. CRUD CLIENTES")
        print("2. CRUD VENDAS")
        print("3. CRUD VENDA ITEM")
        print("4. CRUD PRODUTOS")
        print("5. CRUD CATEGORIA")
        print("0. Sair")
        return input("Opção: ")
    
    @staticmethod
    def menu_clientes():
        while True:
            print("\n--- CRUD CLIENTES ---")
            print("1. Inserir")
            print("2. Listar")
            print("3. Atualizar")
            print("4. Excluir")
            print("0. Voltar")
            op = input("Opção: ")

            if op == "0":
                break
            elif op == "1":
                UI.cliente_inserir()
            elif op == "2":
                UI.cliente_listar()
            elif op == "3":
                UI.cliente_atualizar()
            elif op == "4":
                UI.cliente_excluir()

    @staticmethod
    def menu_categorias():
        while True:
            print("\n--- CRUD CATEGORIA ---")
            print("1. Inserir")
            print("2. Listar")
            print("3. Atualizar")
            print("4. Excluir")
            print("0. Voltar")
            op = input("Opção: ")

            if op == "0":
                break
            elif op == "1":
                UI.categoria_inserir()
            elif op == "2":
                for c in CategoriaDAO.listar():
                    print(c.ToString())
            elif op == "3":
                UI.categoria_atualizar()
            elif op == "4":
                UI.categoria_excluir()

    @staticmethod
    def menu_produtos():
        while True:
            print("\n--- CRUD PRODUTOS ---")
            print("1. Inserir")
            print("2. Listar")
            print("3. Atualizar")
            print("4. Excluir")
            print("0. Voltar")
            op = input("Opção: ")

            if op == "0":
                break
            elif op == "1":
                UI.produto_inserir()
            elif op == "2":
                for p in ProdutoDAO.listar():
                    print(p.ToString())
            elif op == "3":
                UI.produto_atualizar()
            elif op == "4":
                UI.produto_excluir()

    @staticmethod
    def menu_vendas():
        while True:
            print("\n--- CRUD VENDAS ---")
            print("1. Inserir")
            print("2. Listar")
            print("3. Atualizar")
            print("4. Excluir")
            print("0. Voltar")
            op = input("Opção: ")

            if op == "0":
                break
            elif op == "1":
                UI.venda_inserir()
            elif op == "2":
                UI.venda_listar()
            elif op == "3":
                UI.venda_atualizar()
            elif op == "4":
                UI.venda_excluir()

    @staticmethod
    def menu_venda_itens():
        while True:
            print("\n--- CRUD VENDA ITEM ---")
            print("1. Inserir")
            print("2. Listar")
            print("3. Atualizar")
            print("4. Excluir")
            print("0. Voltar")
            op = input("Opção: ")

            if op == "0":
                break
            elif op == "1":
                print("Para inserir um item, você deve realizar uma venda no menu CRUD VENDAS.")
            elif op == "2":
                for i in VendaItemDAO.listar():
                    print(i.ToString())
            elif op == "3":
                UI.vendaitem_atualizar()
            elif op == "4":
                UI.vendaitem_excluir()

    @staticmethod
    def cliente_inserir():
        id = int(input("ID: "))
        n = input("Nome: ")
        f = input("Fone: ")
        e = input("Email: ")
        ClienteDAO.inserir(Cliente(id, n, e, f))

    @staticmethod
    def cliente_listar():
        for c in ClienteDAO.listar(): print(c.ToString())

    @staticmethod
    def cliente_atualizar():
        id = int(input("ID do cliente: "))
        cliente = ClienteDAO.listar_id(id)
        if not cliente:
            print("Cliente não encontrado.")
            return

        nome = input("Novo nome: ")
        email = input("Novo email: ")
        fone = input("Novo fone: ")
        ClienteDAO.atualizar(Cliente(id, nome, email, fone))
        print("Cliente atualizado!")

    @staticmethod
    def cliente_excluir():
        id = int(input("ID do cliente: "))
        if ClienteDAO.excluir(id):
            print("Cliente excluído!")
        else:
            print("Cliente não encontrado.")

    @staticmethod
    def categoria_inserir():
        id = int(input("ID: "))
        c = input("Categoria: ")
        CategoriaDAO.inserir(Categoria(id, c))

    @staticmethod
    def categoria_atualizar():
        id = int(input("ID da categoria: "))
        categoria = CategoriaDAO.listar_id(id)
        if not categoria:
            print("Categoria não encontrada.")
            return

        nome = input("Nova categoria: ")
        CategoriaDAO.atualizar(Categoria(id, nome))
        print("Categoria atualizada!")

    @staticmethod
    def categoria_excluir():
        id = int(input("ID da categoria: "))
        if CategoriaDAO.excluir(id):
            print("Categoria excluída!")
        else:
            print("Categoria não encontrada.")

    @staticmethod
    def produto_inserir():
        id = int(input("ID: "))
        d = input("Descrição: ")
        p = float(input("Preço: "))
        e = int(input("Estoque: "))
        idc = int(input("ID Categoria: "))
        if CategoriaDAO.listar_id(idc):
            ProdutoDAO.inserir(Produto(id, d, p, e, idc))
        else:
            print("Erro: Categoria não existe.")

    @staticmethod
    def produto_atualizar():
        id = int(input("ID do produto: "))
        produto = ProdutoDAO.listar_id(id)
        if not produto:
            print("Produto não encontrado.")
            return

        descricao = input("Nova descrição: ")
        preco = float(input("Novo preço: "))
        estoque = int(input("Novo estoque: "))
        idc = int(input("Nova ID da categoria: "))

        if not CategoriaDAO.listar_id(idc):
            print("Categoria não existe.")
            return

        ProdutoDAO.atualizar(Produto(id, descricao, preco, estoque, idc))
        print("Produto atualizado!")

    @staticmethod
    def produto_excluir():
        id = int(input("ID do produto: "))
        if ProdutoDAO.excluir(id):
            print("Produto excluído!")
        else:
            print("Produto não encontrado.")

    @staticmethod
    def venda_atualizar():
        id = int(input("ID da venda: "))
        venda = VendaDAO.listar_id(id)
        if not venda:
            print("Venda não encontrada.")
            return

        data = input("Nova data: ")
        carrinho = input("Carrinho aberto? (s/n): ").lower() == "s"
        id_cli = int(input("Novo ID Cliente: "))

        if not ClienteDAO.listar_id(id_cli):
            print("Cliente não encontrado.")
            return

        total = float(input("Novo total: "))
        VendaDAO.atualizar(Venda(id, data, carrinho, total, id_cli))
        print("Venda atualizada!")

    @staticmethod
    def venda_excluir():
        id = int(input("ID da venda: "))
        if VendaDAO.excluir(id):
            print("Venda excluída!")
        else:
            print("Venda não encontrada.")

    @staticmethod
    def vendaitem_atualizar():
        id = int(input("ID do item: "))
        item = VendaItemDAO.listar_id(id)
        if not item:
            print("Item não encontrado.")
            return

        qtd = int(input("Nova quantidade: "))
        preco = float(input("Novo preço: "))
        idvenda = int(input("Novo ID da venda: "))
        idproduto = int(input("Novo ID do produto: "))

        if not VendaDAO.listar_id(idvenda):
            print("Venda não encontrada.")
            return

        if not ProdutoDAO.listar_id(idproduto):
            print("Produto não encontrado.")
            return

        VendaItemDAO.atualizar(VendaItem(id, qtd, preco, idvenda, idproduto))
        print("Item atualizado!")

    @staticmethod
    def vendaitem_excluir():
        id = int(input("ID do item: "))
        if VendaItemDAO.excluir(id):
            print("Item excluído!")
        else:
            print("Item não encontrado.")

    @staticmethod
    def venda_inserir():
        id_v = len(VendaDAO.listar()) + 1
        id_cli = int(input("ID Cliente: "))
        if not ClienteDAO.listar_id(id_cli):
            print("Cliente não encontrado.")
            return

        venda = Venda(id_v, "28/04/2026", True, 0, id_cli)
        total = 0

        while True:
            id_p_raw = input("ID Produto (ou 's' p/ sair): ")
            if id_p_raw.lower() == 's':
                break
            try:
                id_p = int(id_p_raw)
            except ValueError:
                print("ID inválido.")
                continue

            prod = ProdutoDAO.listar_id(id_p)
            if prod:
                q = int(input(f"Qtd {prod.get_descricao()}: "))
                item_id = len(VendaItemDAO.listar()) + 1
                item = VendaItem(item_id, q, prod.get_preco(), id_v, id_p)
                VendaItemDAO.inserir(item)
                total += (q * prod.get_preco())
            else:
                print("Produto não encontrado.")

        venda.set_total(total)
        venda.set_carrinho(False)
        VendaDAO.inserir(venda)
        print("Venda gravada!")

    @staticmethod
    def venda_listar():
        for v in VendaDAO.listar():
            print(v.ToString())
            for i in VendaItemDAO.listar():
                if i.get_idvenda() == v.get_id():
                    print(i.ToString())