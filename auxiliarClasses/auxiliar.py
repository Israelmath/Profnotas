from os.path import join, pardir

from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.bubble import Bubble
from kivy.uix.button import Button
from kivy.uix.dropdown import DropDown
from kivy.uix.textinput import TextInput

Builder.load_file(join(__file__, pardir, pardir, 'kvfiles/auxiliar.kv'))


class AlterarGraphBubble(Bubble):
    pass


class Tabela(BoxLayout):
    pass


class SaudacaoBox(BoxLayout):
    pass


class SeparadorHorizontal(BoxLayout):
    pass


class DropMenuTelas(DropDown):
    pass


class AdicionaAnotacao(Button):
    pass

class RedacoesInput(TextInput):
    pass