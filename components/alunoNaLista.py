from os.path import join, pardir

from kivy.app import App
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label

import redis

from components.popups.excluirPop import ExcluirPop
from components.popups.inserirDados import InserirDados

Builder.load_file(join(__file__, pardir, pardir, 'kvfiles/alunoNaLista.kv'))

class AlunoNaLista(BoxLayout):

    def __init__(self, nome, sobrenome, numero, serie, turma, id=0, *args, **kwargs):
        super(AlunoNaLista, self).__init__()
        self.id = id
        self.nome = nome.title()
        self.sobrenome = sobrenome.title()
        self.numero = numero
        self.serie = serie
        self.turma = turma.title()
        # self.ids.info_resumo.spacing = 25

    def cria_box(self, pagina=''):
        if pagina != 'Popup':
            pagina = App.get_running_app().root.current
        if pagina == 'Busca aluno' or pagina == 'Listar alunos':
            tamanho_fonte_nome = 50
            tamanho_fonte_info = 35
        else:
            tamanho_fonte_nome = 38
            tamanho_fonte_info = 27

        # Instancia, e adiciona labels em um BoxLayout com o nome e sobrenome
        box_nome = BoxLayout(size_hint=(0.4, 1), padding=(90, 0, 0, 0))
        lbl_nome = Label(text=self.nome + '\n' + self.sobrenome, color=(1, 1, 1, 1),
                         font_name='Fonts/AmaticSC-Bold.ttf', font_size=tamanho_fonte_nome, size_hint=(0.2, 1),
                         halign='center')
        box_nome.add_widget(lbl_nome)

        # Instancia, e adiciona labels em um BoxLayout com turma, série e número
        box_numero_serie_turma = BoxLayout(orientation='vertical', padding=(90, 0, 0, 0), spacing=20)
        lbl_numero = Label(text='Nº: ' + self.numero, color=(1, 1, 1, 1), font_name='Fonts/AmaticSC-Bold.ttf',
                           font_size=tamanho_fonte_info)
        lbl_serie = Label(text='Série: ' + self.serie + 'º ano', color=(1, 1, 1, 1),
                          font_name='Fonts/AmaticSC-Bold.ttf', font_size=tamanho_fonte_info)
        lbl_turma = Label(text='Turma: ' + self.turma, color=(1, 1, 1, 1), font_name='Fonts/AmaticSC-Bold.ttf',
                          font_size=tamanho_fonte_info)
        box_numero_serie_turma.add_widget(lbl_numero)
        box_numero_serie_turma.add_widget(lbl_serie)
        box_numero_serie_turma.add_widget(lbl_turma)

        btn_excluir = Button(background_normal='Images/excluir.png',
                             border=(0, 0, 0, 0),
                             size_hint=(None, None),
                             size=(35, 35)
                             )
        btn_excluir.bind(on_release=self.excluir)

        btn_info = Button(background_normal='Images/information.png',
                          border=(0, 0, 0, 0),
                          size_hint=(None, None),
                          size=(35, 35)
                          )
        btn_info.bind(on_release=self.info_edicao)

        if pagina == 'Busca aluno' or pagina == 'Listar alunos':
            box_info_excluir = BoxLayout(orientation='vertical', size_hint=(0.2, 1), padding=(25, 0, 0, 0), spacing=10)
            box_info_excluir.add_widget(btn_info)
            box_info_excluir.add_widget(btn_excluir)
            self.ids.info_resumo.add_widget(box_info_excluir)

        adiciona_widgets = [box_nome, box_numero_serie_turma]

        for box in adiciona_widgets:
            self.ids.info_resumo.add_widget(box)

        return self

    def insere_dados(self, *args, **kwargs):
        InserirDados().open()

    def excluir(self, inst):
        ExcluirPop(self.nome, self.sobrenome, self.numero, self.serie, self.turma, self.id).open()

    def info_edicao(self, *args):
        redis.Redis().set('id_aluno', self.id)
        App.get_running_app().root.current = 'Editar info'