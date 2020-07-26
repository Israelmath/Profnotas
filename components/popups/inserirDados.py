from os.path import join, pardir

from kivy.app import App
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.popup import Popup
import redis
from kivy.uix.textinput import TextInput

from DAOs.daoAlunos import search_user, atualiza_notas
from components.popups.excluirPop import ExcluirPop

Builder.load_file(join(__file__, pardir, pardir, pardir, 'kvfiles/inserirDados.kv'))


class InserirDados(Popup):

    def __init__(self, *args, **kwargs):
        super().__init__()

        self.id_professor = redis.Redis().get('id_professor').decode('utf-8')
        self.id = redis.Redis().get('id_aluno').decode('utf-8')
        self.title = 'Cuidado!\nVocê está alterando informações'
        self.title_align = 'center'
        self.title_font = 'Fonts/AmaticSC-Bold.ttf'
        self.title_color = 0, 0, 0, 1
        self.title_size = 30
        self.background = 'white'
        self.aluno_lista = []
        self.aluno_instanciado = ''
        self.trimestre = 0
        self.rec = -1
        self.part = -1

        self.aluno_lista = search_user(self.id, 'Id', self.id_professor)[0]
        self.aluno_instanciado = AlunoNaLista(id=self.aluno_lista[0],
                                              nome=self.aluno_lista[1].title(),
                                              sobrenome=self.aluno_lista[2].title(),
                                              turma=self.aluno_lista[3].title(),
                                              serie=str(self.aluno_lista[4]),
                                              numero=str(self.aluno_lista[5]))
        self.ids.info_aluno.add_widget(self.aluno_instanciado.cria_box(pagina='Popup'))

        btn_rec = Button(text='Editar',
                         halign='center',
                         size_hint=(0.25, 0.5),
                         pos_hint={'center_y': 0.5},
                         font_name='Fonts/AmaticSC-Bold.ttf',
                         font_size=21,
                         color=(0, 0, 0, 1),
                         background_normal='',
                         background_color=(209 / 255, 242 / 255, 165 / 255, 1))
        btn_rec.bind(on_release=self.add_rec_input)
        self.ids.rec.add_widget(btn_rec)

        btn_part = Button(text='Editar',
                          halign='center',
                          size_hint=(0.25, 0.5),
                          pos_hint={'center_y': 0.5},
                          font_name='Fonts/AmaticSC-Bold.ttf',
                          font_size=21,
                          color=(0, 0, 0, 1),
                          background_normal='',
                          background_color=(209 / 255, 242 / 255, 165 / 255, 1))
        btn_part.bind(on_release=self.add_part_input)
        self.ids.part.add_widget(btn_part)

    def primeiro_tri(self, inst):
        self.ids.trimestre.text = '1º Trimestre'
        self.trimestre = 1

    def segundo_tri(self, inst):
        self.ids.trimestre.text = '2º Trimestre'
        self.trimestre = 2

    def terceiro_tri(self, inst):
        self.ids.trimestre.text = '3º Trimestre'
        self.trimestre = 3

    def insere_info(self):
        ids_pop = self.ids
        id_professor = redis.Redis().get('id_professor').decode('utf-8')

        for id in ids_pop:
            if id in ['red1', 'red2', 'red3', 'red4', 'qtd', 'prova']:
                if ids_pop[id].text == '':
                    self.ids[id].text = '-1'

        if ids_pop.rec.children[0].text == 'Editar':
            self.part = '-1'
        else:
            self.rec = self.ids.rec.children[0].text

        if ids_pop.part.children[0].text == 'Editar':
            red_feitas = float(ids_pop['qtd'].text)
            calcula_participacao = red_feitas / 4
            self.part = calcula_participacao * 2
        else:
            self.part = self.ids.part.children[0].text

        notas = {'R1': self.ids.red1.text,
                 'R2': self.ids.red2.text,
                 'R3': self.ids.red3.text,
                 'R4': self.ids.red4.text,
                 'Participacao': self.part,
                 'Qtd': self.ids.qtd.text,
                 'Prova': self.ids.prova.text,
                 'Rec': self.rec,
                 'trimestre': self.trimestre,
                 'Id': self.id}

        atualiza_notas(notas, id_professor)

    def add_rec_input(self, *args):

        rec = TextInput(font_size=25,
                        size_hint=(None, None),
                        width=50,
                        height=40,
                        padding=(20, 0, 0, 0),
                        pos_hint={'top': 0.7, 'right': 1},
                        multiline=False,
                        write_tab=False)
        self.ids.rec.clear_widgets()
        self.ids.rec.add_widget(rec)

    def add_part_input(self, *args):

        part = TextInput(font_size=25,
                         size_hint=(None, None),
                         width=50,
                         height=40,
                         padding=(20, 0, 0, 0),
                         pos_hint={'top': 0.7, 'right': 1},
                         multiline=False,
                         write_tab=False)
        self.ids.part.clear_widgets()
        self.ids.part.add_widget(part)


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
