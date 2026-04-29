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