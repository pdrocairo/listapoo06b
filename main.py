from view.ui import UI
from dao.cliente_dao import ClienteDAO
from dao.categoria_dao import CategoriaDAO
from dao.produto_dao import ProdutoDAO
from dao.venda_dao import VendaDAO
from dao.venda_item_dao import VendaItemDAO

def main():
    
    try:
        ClienteDAO.abrir()
        CategoriaDAO.abrir()
        ProdutoDAO.abrir()
        VendaDAO.abrir()
        VendaItemDAO.abrir()
        print("Dados carregados com sucesso!")
    except Exception as e:
        print(f"Aviso: Erro ao carregar dados ou arquivos inexistentes: {e}")

   
    UI.main()


if __name__ == "__main__":
    main()