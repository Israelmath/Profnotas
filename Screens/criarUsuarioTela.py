from os.path import join, pardir

from kivy.app import App
from kivy.clock import Clock
from kivy.lang import Builder
from kivy.uix.screenmanager import Screen

from DAOs.ConfigDB import busca_banco, inicia_banco, insere_professor

Builder.load_file(join(__file__, pardir, pardir, 'kvfiles/criarUsuarioTela.kv'))

class CriarUsuarioTela(Screen):

    def verifica(self, *args):
        ids_tela = self.ids
        info_faltante = False
        for id in ids_tela:
            if id != 'verificacao' and ids_tela[id].text == '':
                info_faltante = True
                Clock.schedule_once(self.apaga_notificacao, 4)
                ids_tela.verificacao.text = 'Falta alguma informação. Tente novamente.'

        if ids_tela.senha.text != ids_tela.confirmacao.text and not info_faltante:
            Clock.schedule_once(self.apaga_notificacao, 4)
            ids_tela.confirmacao.text = ''
            ids_tela.verificacao.text = 'As senhas não batem. Tente novamente.'
        else:
            if busca_banco(ids_tela.login.text.title()) and not info_faltante:
                Clock.schedule_once(self.apaga_notificacao, 4)
                ids_tela.verificacao.text = 'Já existe um banco com esse nome.'
            elif not info_faltante:
                inicia_banco(ids_tela.login.text.title())
                professor = {'Nome': ids_tela.nome.text.title(),
                             'Sobrenome': ids_tela.sobrenome.text.title(),
                             'Disciplina': ids_tela.disciplina.text.title(),
                             'Senha': ids_tela.senha.text}
                insere_professor(professor, ids_tela.login.text.title())
                App.get_running_app().root.current = 'Tela de login'
                for id in ids_tela:
                    ids_tela[id].text = ''

    def verifica_login(self, *args):
        if self.ids.login.text.title() != '':
            if busca_banco(self.ids.login.text.title()):
                Clock.schedule_once(self.apaga_notificacao, 4)
                self.ids.verificacao.text = f'Esse login "{self.ids.login.text.title()}" já está sendo usado'

    def apaga_notificacao(self, *args):
        self.ids.verificacao.text = ''
