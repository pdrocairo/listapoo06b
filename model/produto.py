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