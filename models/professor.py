import redis

class Professor:

    def __init__(self):
        self.request = redis.Redis(host='localhost', port=6379, db=0)
        self.__nome = ''

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, novo_nome):
        self.request.set('id_professor', novo_nome)
        self.__nome = novo_nome