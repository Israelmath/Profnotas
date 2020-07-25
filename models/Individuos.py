
class Usuario:

    def __init__(self, id, nome, sobrenome, turma, serie, numero):
        self.__id = id
        self.__nome = nome.title()
        self.__sobrenome = sobrenome.title()
        self.__turma = turma
        self.__serie = serie
        self.__numero = -1
        self.__media1 = -1
        self.__media2 = -1
        self.__media3 = -1
        self.__mediaF = -1

    @property
    def serie(self):
        return self.__serie

    @property
    def sobrenome(self):
        return self.__sobrenome

    @property
    def turma(self):
        return self.__turma

    @property
    def id(self):
        return self.__id

    @property
    def nome(self):
        return self.__nome

    @property
    def numero(self):
        return self.__numero

    @property
    def media1(self):
        return self.__media1
    
    @property
    def media2(self):
        return self.__media2

    @property
    def media3(self):
        return self.__media3

    @property
    def mediaF(self):
        return self.__mediaF

    @id.setter
    def id(self, novo_id):
        self.__id = novo_id

    @nome.setter
    def nome(self, novo_nome):
        self.__nome = novo_nome

    @sobrenome.setter
    def sobrenome(self, novo_sobrenome):
        self.__sobrenome = novo_sobrenome

    @turma.setter
    def turma(self, nova_turma):
        self.__turma = nova_turma

    @serie.setter
    def serie(self, nova_serie):
        self.__serie = nova_serie
    
    @numero.setter
    def numero(self, novo_numero):
        self.__numero = novo_numero
    
    @media1.setter
    def media1(self, nova_media1):
        self.__media1 = nova_media1

    @media2.setter
    def media2(self, nova_media2):
        self.__media2 = nova_media2

    @media3.setter
    def media3(self, nova_media3):
        self.__media3 = nova_media3

    @mediaF.setter
    def mediaF(self, nova_mediaF):
        self.__mediaF = nova_mediaF

    def __str__(self):
        return '{},{}'.format(self.nome, self.id)