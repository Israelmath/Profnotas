from os.path import join, pardir

from kivy.lang import Builder
from kivy.uix.screenmanager import Screen
import redis

from DAOs.daoAlunos import search_user
from components.alunoNaLista import AlunoNaLista

Builder.load_file(join(__file__, pardir, pardir, 'kvfiles/buscaAlunoTela.kv'))


class BuscaAlunoTela(Screen):

    def on_pre_enter(self, *args):
        self.ids.alunos_buscados.clear_widgets()
        print(self.ids.busca_aluno_bar)

    def busca(self, from_update=False):
        id_professor = redis.Redis().get('id_professor').decode('utf-8')

        self.ids.alunos_buscados.clear_widgets()
        nome = self.ids.busca_aluno_bar.text
        if nome.isalpha():
            alunos = search_user(nome, 'Nome', banco=id_professor)
        else:
            alunos = search_user(nome, 'Numero', banco=id_professor)
        if not from_update:
            self.adiciona_alunos(alunos)
        else:
            return alunos

    def update(self):
        self.ids.alunos_buscados.clear_widgets()
        alunos = self.busca(from_update=True)
        self.adiciona_alunos(alunos)

    def adiciona_alunos(self, alunos=[]):
        for aluno in alunos:
            instancia_AlunoNaLista = AlunoNaLista(id=aluno[0],
                                                  nome=aluno[1].title(),
                                                  sobrenome=aluno[2].title(),
                                                  turma=aluno[3].title(),
                                                  serie=str(aluno[4]),
                                                  numero=str(aluno[5])
                                                  )
            self.ids.alunos_buscados.add_widget(instancia_AlunoNaLista.cria_box())