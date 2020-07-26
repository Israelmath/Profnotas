from os.path import join, pardir

from kivy.app import App
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.popup import Popup
import redis

from DAOs.daoAlunos import del_user

Builder.load_file(join(__file__, pardir, pardir, pardir, 'kvfiles/excluirPop.kv'))

class ExcluirPop(Popup):

    def __init__(self, nome, sobrenome, numero, serie, turma, id, **kwargs):
        super().__init__(**kwargs)

        self.id_professor = redis.Redis().get('id_professor').decode('utf-8')
        self.title = 'Cuidado! Você irá excluir o(a) aluno(a) abaixo!'
        self.title_font = 'Fonts/AmaticSC-Bold.ttf'
        self.title_size = 25
        self.title_color = 0, 0, 0, 1
        self.background = 'white'
        self.id = id
        self.nome = nome
        self.sobrenome = sobrenome
        self.numero = numero
        self.serie = serie
        self.turma = turma

        aluno = [self.nome, self.sobrenome, self.numero, self.serie, self.turma]
        info = f'Nome: {aluno[0]} {aluno[1]}\nNúmero: {aluno[2]}\nSérie: {aluno[3]}\nTurma: {aluno[4]}'

        bigbox = BoxLayout(orientation='vertical')
        box_sup = BoxLayout(orientation='vertical', size_hint=(1, 0.7), padding=(0, 0, 0, 50))
        box_inf = BoxLayout(orientation='horizontal', size_hint=(1, 0.3), spacing=5, padding=5)

        box_sup.add_widget(Label(text='Você tem certeza que quer escluir o(a) aluno(a):',
                                 color=(0, 0, 0, 1),
                                 size_hint=(1, 0.1),
                                 font_name='Fonts/AmaticSC-Bold.ttf',
                                 font_size=25)
                           )

        box_sup.add_widget(Label(text=info,
                                 color=(0, 0, 0, 1),
                                 size_hint=(1, 0.1),
                                 font_name='Fonts/AmaticSC-Bold.ttf',
                                 font_size=30,
                                 halign='left')
                           )
        bigbox.add_widget(box_sup)

        btn_sim = Button(text='Sim')
        btn_sim.bind(on_release=self.deletar)
        btn_nao = Button(text='Não')
        btn_nao.bind(on_release=self.dismiss)
        box_inf.add_widget(btn_sim)
        box_inf.add_widget(btn_nao)

        bigbox.add_widget(box_inf)

        self.add_widget(bigbox)

    def deletar(self, *args):
        id_professor = redis.Redis().get('id_professor').decode('utf-8')

        del_user(self.id, id_professor)
        current_screen_name = App.get_running_app().root.current
        current_screen_inst = App.get_running_app().root.get_screen(current_screen_name)
        current_screen_inst.update()
        self.dismiss()