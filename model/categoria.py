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