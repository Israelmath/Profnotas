from os.path import join, pardir

from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label

Builder.load_file(join(__file__, pardir, pardir, 'kvfiles/boxMedias.kv'))

class BoxMedias(BoxLayout):

    def __init__(self, media1, media2, media3, mediaf, *args, **kwargs):
        super(BoxMedias, self).__init__(orientation='vertical', padding=(0, 15, 0, 0))
        self.media1 = str(media1)
        self.media2 = str(media2)
        self.media3 = str(media3)
        self.mediaf = str(mediaf)

    def cria_box(self):
        titulo = Label(text='Médias',
                       color=(0, 0, 0, 1),
                       size_hint=(1, 0.1),
                       pos_hint={'center': 1},
                       font_name='Fonts/AmaticSC-Bold.ttf',
                       font_size=45,
                       underline=True)

        grid_medias = GridLayout(cols=2, padding=(3, 10, 3, 3), spacing=3)
        box_medias = BoxLayout(orientation='vertical')
        box_mediaf = BoxLayout()

        lbl_media1 = Label(text='[size=25]1º trimestre[/size]:   [size=40]' + self.media1 + '[/size]',
                           color=(0, 0, 0, 1), font_name='Fonts/AmaticSC-Bold.ttf', halign='center', markup=True)
        lbl_media2 = Label(text='[size=25]2º trimestre[/size]:   [size=40]' + self.media2 + '[/size]',
                           color=(0, 0, 0, 1), font_name='Fonts/AmaticSC-Bold.ttf', halign='center', markup=True)
        lbl_media3 = Label(text='[size=25]3º trimestre[/size]:   [size=40]' + self.media3 + '[/size]',
                           color=(0, 0, 0, 1), font_name='Fonts/AmaticSC-Bold.ttf', halign='center', markup=True)
        lbl_mediaf = Label(text='[size=40]Média final[/size]:   [size=40]\n' + self.mediaf + '[/size]',
                           color=(0, 0, 0, 1), font_name='Fonts/AmaticSC-Bold.ttf', halign='center', markup=True)

        labels = [lbl_media1, lbl_media2, lbl_media3]
        for lbl in labels:
            box_medias.add_widget(lbl)
        box_mediaf.add_widget(lbl_mediaf)

        grid_medias.add_widget(box_medias)
        grid_medias.add_widget(box_mediaf)

        self.add_widget(titulo)
        self.add_widget(grid_medias)

        return self