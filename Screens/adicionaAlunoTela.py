from os.path import join, pardir

from kivy.app import App
from kivy.clock import Clock
from kivy.lang import Builder
from kivy.uix.screenmanager import Screen

Builder.load_file(join(__file__, pardir, pardir, 'kvfiles/adicionaAlunoTela.kv'))

class AdicionaAlunoTela(Screen):

    def verifica_entrada(self, *args, **kwargs):
        print(args)
        if args[0][1] == 13 or args[0][1] == 271:
            tela_atual = App.get_running_app().root.current
            if tela_atual == 'Adiciona aluno':
                self.verifica_info()

    def verifica_info(self):
        info_alunos = self.ids.form
        if info_alunos.ids.Nome.text != '':
            info_alunos.insere()
            Clock.schedule_once(self.limpa_info, 3)
            self.ids.verificacao.color = (119 / 255, 150 / 255, 1, 0.7)
            self.ids.verificacao.font_size = 20
            self.ids.verificacao.text = 'Inserindo aluno(a) no banco de dados. Aguarde...'
        else:
            Clock.schedule_once(self.limpa_info, 4)
            self.ids.verificacao.color = (1, 64 / 255, 64 / 255, 0.7)
            self.ids.verificacao.font_size = 15
            self.ids.verificacao.text = 'Você precisa informar algum aluno.'

    def limpa_info(self, *args):
        self.ids.verificacao.text = ''