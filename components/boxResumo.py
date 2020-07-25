from os.path import join, pardir

from kivy.lang import Builder
from components.alunoNaLista import AlunoNaLista

Builder.load_file(join(__file__, pardir, pardir, 'kvfiles/boxResumo.kv'))


class BoxResumo(AlunoNaLista):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    pass
