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

    def get_info_aluno(self, text, nome, *args):
        ids_tela = self.ids
        not_check = ['form', 'verificacao', 'btn_config']
        show_btn_confirm = True
        if nome == 'Nome':
            ids_tela.show_NomeSobrenome.text = text.title()
        if nome == 'Sobrenome':
            if ids_tela.show_NomeSobrenome.text != '':
                ids_tela.show_NomeSobrenome.text = ids_tela.show_NomeSobrenome.text
        if nome == 'Numero':
            ids_tela.show_Numero.text = text.title()
        if nome == 'Serie':
            ids_tela.show_Serie.text = text.title()
        if nome == 'Turma':
            ids_tela.show_Turma.text = text.title()

        for id in ids_tela:
            if id not in not_check:
                if ids_tela[id].text == '':
                    show_btn_confirm = False

        self.change_btn_confirm(show_btn_confirm)

    def change_btn_confirm(self, show_btn):
        id_btn = self.ids.btn_config
        if show_btn:
            id_btn.padding = (0, 50)
            id_btn.size_hint = (None, None)
            id_btn.size = (200, 60)
            id_btn.pos_hint = {'center_x': 0.5, 'center_y': 0.5}
            id_btn.border = (0, 0, 0, 0)
            id_btn.text = 'Confirmar inscrição'
            id_btn.font_name = 'Fonts/AmaticSC-Bold.ttf'
            id_btn.color = (0, 0, 0, 1)
            id_btn.font_size = 24
            id_btn.background_color = (1, 1, 1, 1)
        else:
            id_btn.background_normal = ''
            id_btn.background_color = (0, 0, 0, 0)