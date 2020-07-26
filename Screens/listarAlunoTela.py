from os.path import join, pardir

import redis
from kivy.lang import Builder
from kivy.uix.screenmanager import Screen

from DAOs.daoAlunos import list_all
from components.alunoNaLista import AlunoNaLista

Builder.load_file(join(__file__, pardir, pardir, 'kvfiles/listarAlunoTela.kv'))

class ListarAlunoTela(Screen):


    def update(self):
        id_professor = redis.Redis().get('id_professor').decode('utf-8')
        print(self.ids)

        self.ids.lista_de_alunos.clear_widgets()
        alunos = list_all(id_professor)
        for aluno in alunos:
            elemento = AlunoNaLista(id=aluno[0],
                                    nome=aluno[1].title(),
                                    sobrenome=aluno[2].title(),
                                    turma=aluno[3].title(),
                                    serie=str(aluno[4]),
                                    numero=str(aluno[5])
                                    )
            self.ids.lista_de_alunos.add_widget(elemento.cria_box())

    def on_pre_enter(self, *args):
        self.update()