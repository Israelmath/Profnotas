from calendar import Calendar, monthrange
from os.path import join, pardir
from time import localtime

from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.screenmanager import Screen

from auxiliarClasses.auxiliar import SaudacaoBox
from models.anotacoes import Anotacoes

Builder.load_file(join(__file__, pardir, pardir, 'kvfiles/calendarioTela.kv'))

class CalendarioTela(Screen):

    def __init__(self, *args, **kwargs):
        super().__init__()
        self.mes = localtime().tm_mon
        self.ano = localtime().tm_year
        self.dia_semana = ['S', 'T', 'Q', 'Q', 'S', 'S', 'D']
        self.nome_mes = ['janeiro', 'fevereiro', 'março', 'abril', 'maio', 'junho', 'julho', 'agosto', 'setembro',
                         'outubro', 'novembro', 'dezembro']

    def on_pre_enter(self):
        self.mes = localtime().tm_mon
        self.ano = localtime().tm_year
        ids_tela = self.ids
        for id in ids_tela:
            ids_tela[id].clear_widgets()

        self.cria_mes_ano()
        self.cria_linha_semana()
        self.cria_mes(self.mes, self.ano)
        self.ids.anotacoes.add_widget(Anotacoes())

    def cria_mes_ano(self):
        mes = self.mes - 1
        ano = self.ano

        self.ids.mes_e_ano.text = f'{self.nome_mes[mes].title()} - {ano}'

    def cria_linha_semana(self):

        c = Calendar(firstweekday=6)
        for i in c.iterweekdays():
            box = BoxLayout()
            lbl_dia_semana = Label(text=self.dia_semana[i],
                                   size_hint=(1, 0.5),
                                   color=(0, 0, 0, 1))
            box.add_widget(lbl_dia_semana)
            self.ids.datas.add_widget(box)
        for i in c.iterweekdays():
            self.ids.datas.add_widget(BoxLayout(size_hint=(0.2, 0.2)))

    def cria_mes(self, mes, ano):
        week_days = monthrange(self.ano, self.mes)
        dia = localtime().tm_mday
        mes = localtime().tm_mon
        ano = localtime().tm_year
        i = 0
        for d in range(week_days[1]):
            while i <= week_days[0]:
                self.ids.datas.add_widget(BoxLayout())
                i += 1
            lbl_dia = Label(text=f'{d + 1}',
                            color=(0, 0, 0, 1),
                            font_name='Fonts/AmaticSC-Bold.ttf',
                            font_size=20)
            if (dia == d + 1) and (ano == self.ano) and (mes == self.mes):
                box = SaudacaoBox()
            else:
                box = BoxLayout()
            box.add_widget(lbl_dia)
            self.ids.datas.add_widget(box)

    def proximo_mes(self):
        self.mes += 1
        if self.mes > 12:
            self.mes = 1
            self.ano += 1

        self.ids.datas.clear_widgets()
        self.cria_mes_ano()
        self.cria_linha_semana()
        self.cria_mes(self.mes, self.ano)

    def volta_mes(self):
        self.mes -= 1
        if self.mes < 1:
            self.mes = 12
            self.ano -= 1

        self.ids.datas.clear_widgets()
        self.cria_mes_ano()
        self.cria_linha_semana()
        self.cria_mes(self.mes, self.ano)

        # def teste(self):
        print(self.ids.anotacoes.children[0].ids.notas.children)