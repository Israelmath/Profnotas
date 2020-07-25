from os.path import join, pardir

from kivy.app import App
from kivy.lang import Builder
from kivy.uix.behaviors import ButtonBehavior
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.image import Image


Builder.load_file(join(__file__, pardir, pardir, 'kvfiles/imagemInicial.kv'))


class ImagemInicial(BoxLayout, ButtonBehavior, Image):

    def __init__(self, image_source, image_caption, *args, **kwargs):
        super(ImagemInicial, self).__init__()
        self.image_source = image_source
        self.image_caption = image_caption

    def btn_press(self, instance):
        source = instance.image_source
        if source == 'Images/Adiciona_aluno.jpg':
            App.get_running_app().root.current = 'Adiciona aluno'
        elif source == 'Images/Busca_aluno.png':
            App.get_running_app().root.current = 'Busca aluno'
        elif source == 'Images/Lista_alunos.png':
            App.get_running_app().root.current = 'Listar alunos'
        elif source == 'Images/Envia_email.png':
            App.get_running_app().root.current = 'Calendario'
        else:
            print(f'Tela "{source}" ainda não foi criada')