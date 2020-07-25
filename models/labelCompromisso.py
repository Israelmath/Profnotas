from os.path import join, pardir

from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout

Builder.load_file(join(__file__, pardir, pardir, 'kvfiles/labelCompromisso.kv'))

class LabelCompromisso(BoxLayout):

    def __init__(self, info, instance, **kwargs):
        super().__init__()
        self.ids.Titulo.text = info['Titulo']
        self.ids.Data.text = info['Data']
        self.ids.Comentario.text = info['Anotacao']
        self.size_hint = (None, None)
        self.width = instance.width * 0.8
        self.height = 80
        self.pos_hint = {'center_x': 0.55, 'center_y': 0.5}

        print(f'instance: {instance}')
        print(self.width)