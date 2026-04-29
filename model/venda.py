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