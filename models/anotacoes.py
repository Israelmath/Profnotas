from os.path import pardir, join

from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout

from auxiliarClasses.auxiliar import AdicionaAnotacao
from models.notaCompromisso import NotaCompromisso

Builder.load_file(join(__file__, pardir, pardir, 'kvfiles/anotacoes.kv'))


class Anotacoes(BoxLayout):

    def apresenta_compromisso(self):
        self.ids.notas.add_widget(AdicionaAnotacao(text='Olá!',
                                                   size_hint=(None, None),
                                                   width=250,
                                                   height=50,
                                                   pos_hint={'center_x': 0.55, 'center_y': 0.5},
                                                   background_color=(0, 0, 0, 0),
                                                   font_size=35,
                                                   color=(0, 0, 0, 1))
                                  )

    def cria_compromisso(self):
        self.ids.notas.add_widget(NotaCompromisso(size_hint=(None, None),
                                                  pos_hint={'center_x': 0.6, 'center_y': 0.8},
                                                  width=self.parent.width * 0.7,
                                                  height=self.parent.height * 0.4
                                                  )
                                  )
