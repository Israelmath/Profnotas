from time import localtime

from kivy.clock import Clock
from kivy.lang import Builder
from kivy.uix.screenmanager import Screen
from os.path import join
from os import pardir

from DAOs.ConfigDB import busca_info
from components.imagemInicial import ImagemInicial
import redis

Builder.load_file(join(__file__, pardir, pardir, 'kvfiles/menuPrincipal.kv'))

class MenuPrincipal(Screen):

    def __init__(self, *args, **kwargs):
        super().__init__()

        btn_ad_aluno = ImagemInicial(image_source='Images/Adiciona_aluno.jpg', image_caption='Adicionar aluno',
                                     texture_size=(60, 60))
        btn_lista_alunos = ImagemInicial(image_source='Images/Lista_alunos.png', image_caption='Listar alunos',
                                         texture_size=(60, 60))
        btn_envia_email = ImagemInicial(image_source='Images/Envia_email.png', image_caption='Enviar relatório',
                                        texture_size=(60, 60))
        btn_atualiza_info = ImagemInicial(image_source='Images/Busca_aluno.png', image_caption='Buscar aluno',
                                          texture_size=(60, 60))

        self.ids.botoes_menu_principal.add_widget(btn_ad_aluno)
        self.ids.botoes_menu_principal.add_widget(btn_lista_alunos)
        self.ids.botoes_menu_principal.add_widget(btn_envia_email)
        self.ids.botoes_menu_principal.add_widget(btn_atualiza_info)

    def on_pre_enter(self, *args):
        id_professor = redis.Redis().get('id_professor').decode('utf-8')

        ids_tela = self.ids
        professor = busca_info(id_professor)
        print({f'professor: {professor}'})
        dia_da_semana = ['Segunda-feira', 'Terça-feira', 'Quarta-feira', 'Quinta-feira', 'Sexta-feira', 'Sábado',
                         'Domingo']
        mes = ['janeiro', 'fevereiro', 'março', 'abril', 'maio', 'junho', 'julho', 'agosto', 'setembro', 'outubro',
               'novembro', 'dezembro']

        horas = localtime().tm_hour
        if horas >= 0 and horas < 6:
            ids_tela.saudacao.text = f"Boa madrugada, {professor[3]}!"
        elif horas >= 6 and horas < 12:
            ids_tela.saudacao.text = f'Bom dia, {professor[3]}!'
        elif horas >= 12 and horas < 18:
            ids_tela.saudacao.text = f'Boa tarde, {professor[3]}!'
        elif horas >= 18 and horas <= 23:
            ids_tela.saudacao.text = f'Boa noite, {professor[3]}!'

        ids_tela.data.text = f'{dia_da_semana[localtime().tm_wday]}, {localtime().tm_mday} de {mes[localtime().tm_mon]}'
        self.atualiza_hora()
        Clock.schedule_interval(self.atualiza_hora, 10)

    def atualiza_hora(self, *args):
        self.ids.hora.text = ''
        self.ids.hora.text = f'{localtime().tm_hour}: {localtime().tm_min}'