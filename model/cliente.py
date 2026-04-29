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