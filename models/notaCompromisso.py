from os.path import join, pardir

from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
import redis

from DAOs.daoCompromissos import salva_compromisso
from funcoes.funcoes import analisa_data
from models.labelCompromisso import LabelCompromisso

Builder.load_file(join(__file__, pardir, pardir, 'kvfiles/notaCompromisso.kv'))

class NotaCompromisso(BoxLayout):


    def guardar_compromisso(self, *args):

        id_professor = redis.Redis().get('id_professor').decode('utf-8')

        inst_compromisso = args[0]
        ids_compromisso = inst_compromisso.ids
        compromisso = {
            'Titulo': ids_compromisso['Titulo'].text,
            'Data': analisa_data(ids_compromisso['Data'].text),
            'Anotacao': ids_compromisso['Anotacao'].text,
            'Cor': ''
        }

        salva_compromisso(compromisso, id_professor)

        self.atualiza_label(compromisso, inst_compromisso.parent, inst_compromisso)

    def atualiza_label(self, compromisso, wd_pai, wd_filho):
        lbl_compromisso = LabelCompromisso(compromisso, wd_pai.parent)
        wd_pai.remove_widget(wd_filho)
        wd_pai.add_widget(lbl_compromisso)
