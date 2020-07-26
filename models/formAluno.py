from os.path import join, pardir

from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
import redis

from DAOs.daoAlunos import insere_aluno

Builder.load_file(join(__file__, pardir, pardir, 'kvfiles/formAluno.kv'))

class FormAluno(BoxLayout):

    def insere(self, *args):
        ids_tela = self.ids
        id_professor = redis.Redis().get('id_professor').decode('utf-8')

        insere_aluno(ids_tela['Nome'].text.strip().title(),
                     ids_tela['Sobrenome'].text.strip().title(),
                     ids_tela['Turma'].text.strip().title(),
                     ids_tela['Serie'].text.strip().title(),
                     ids_tela['Numero'].text.strip(),
                     banco=id_professor
                     )
        for id in ids_tela:
            ids_tela[id].text = ''