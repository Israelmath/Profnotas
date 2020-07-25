import redis

class Aluno:

    def __init__(self):
        self.request = redis.Redis(host='localhost', port=6379, db=0)
        self.__numero = ''

    @property
    def numero(self):
        return self.__numero

    @numero.setter
    def numero(self, novo_numero):
        self.request.set('id_aluno', novo_numero)
        self.__numero = novo_numero