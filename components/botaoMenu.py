from os.path import join, pardir

from kivy.app import App
from kivy.lang import Builder
from kivy.uix.button import Button

Builder.load_file(join(__file__, pardir, pardir, 'kvfiles/botaoMenu.kv'))

class BotaoMenu(Button):

    def sair(self, *args):
        App.get_running_app().root.get_screen('Menu inicial').sair()

    def open(self, *args):
        self.ids.menu.open(self)