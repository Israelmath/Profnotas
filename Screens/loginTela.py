from kivy.app import App
from kivy.clock import Clock
from kivy.lang import Builder
from kivy.uix.image import Image
from kivy.core.window import Window
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.popup import Popup
from kivy.uix.screenmanager import Screen
from os.path import join, pardir
from os import getcwd

import Graphs
from DAOs.DBConfig import busca_banco, busca_info
from models.professor import Professor

Builder.load_file(join(__file__, pardir, pardir, 'kvfiles/loginTela.kv'))

class LoginTela(Screen):

    def on_pre_enter(self):
        Window.bind(on_request_close=self.sair)
        Window.bind(on_keyboard=self.verifica)

    def verifica(self, *args):
        tela = App.get_running_app().root.current
        inst_tela = App.get_running_app().root.get_screen(tela)
        if args[1] == 13 or args[1] == 271:
            if tela == 'Tela de login':
                self.entra()
            elif tela == 'Cria usuario':
                inst_tela.verifica()
            elif tela == 'Adiciona aluno':
                inst_tela.verifica_entrada(args)
        elif args[1] == 27:
            if tela == 'Menu inicial' or tela == 'Tela de login':
                self.sair()
            elif tela == 'Cria usuario':
                App.get_running_app().root.current = 'Tela de login'
            elif tela != 'Cria usuario':
                App.get_running_app().root.current = 'Menu inicial'
        return True

    def entra(self, *args):

        ids_tela = self.ids
        if busca_banco(ids_tela.login.text.title()):
            senha = busca_info(ids_tela.login.text.title(), senha=True)[0]
            if senha == ids_tela.senha.text:
                Professor().nome = ids_tela.login.text.title()
                App.get_running_app().root.current = 'Menu inicial'
            elif ids_tela.login.text != '' or ids_tela.senha.text != '':
                Clock.schedule_once(self.limpa_info, 4)
                ids_tela.verificacao.text = 'Login ou senha incorretos. Tente novamente.'
        else:
            Clock.schedule_once(self.limpa_info, 4)
            ids_tela.verificacao.text = 'Login ou senha incorretos. Tente novamente.'

    def limpa_info(self, *args):
        self.ids.login.text = ''
        self.ids.senha.text = ''
        self.ids.verificacao.text = ''

    def sair(self, *args, **kwargs):
        pop_sair = BoxLayout(orientation='vertical', spacing=15, padding=(0, 5, 0, 5))
        botoes = BoxLayout(spacing=20)

        pop = Popup(title='Deseja mesmo sair?', content=pop_sair, size_hint=(None, None), size=(300, 180))

        sim = Button(text='Sim', size_hint=(0.3, 1), on_release=self.limpa_tudo)
        nao = Button(text='Não', size_hint=(0.3, 1), on_release=pop.dismiss)

        botoes.add_widget(sim)
        botoes.add_widget(nao)

        atencao = Image(source=join(getcwd(), 'Images/error.png'))

        pop_sair.add_widget(atencao)
        pop_sair.add_widget(botoes)

        pop.open()
        return True

    def limpa_tudo(self, *args):
        App.get_running_app().stop()
        Graphs.Graficos.deleta_graficos(self)