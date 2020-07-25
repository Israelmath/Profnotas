from os.path import join, pardir

from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label

from Verificadores import calcula_media_trimestral

Builder.load_file(join(__file__, pardir, pardir, 'kvfiles/notasAluno.kv'))


class NotasAluno(BoxLayout):

    def __init__(self, id, trimestre, red1, red2, red3, red4, part, qtd, prova, rec, *args, **kwargs):
        super(NotasAluno, self).__init__(orientation='vertical', size_hint_y=None, height=270, spacing=15,
                                         padding=(0, 20, 0, 20))
        self.id = id
        self.trimestre = str(trimestre)
        if red1 < 0:
            self.red1 = '0'
        else:
            self.red1 = str(red1)

        if red2 < 0:
            self.red2 = '0'
        else:
            self.red2 = str(red2)

        if red3 < 0:
            self.red3 = '0'
        else:
            self.red3 = str(red3)

        if red4 < 0:
            self.red4 = '0'
        else:
            self.red4 = str(red4)

        if part < 0:
            self.part = '0'
        else:
            self.part = str(part)

        if qtd < 0:
            self.qtd = '0'
        else:
            self.qtd = str(qtd)

        if prova < 0:
            self.prova = '0'
        else:
            self.prova = str(prova)

        if rec < 0:
            self.rec = '0'
        else:
            self.rec = str(rec)

    def cria_box(self, *args):
        notas = [self.red1, self.red2, self.red3, self.red4, self.qtd, self.prova, self.rec]

        notas = [float(valor) for valor in notas]
        media = calcula_media_trimestral(notas[0], notas[1], notas[2], notas[3], notas[4], notas[5], notas[6])

        box_integral = GridLayout(cols=2, spacing=3, size_hint=(1, 0.9))

        box_redacoes = BoxLayout(orientation='vertical')
        box_avaliacoes = BoxLayout(orientation='vertical')

        lbl_red1 = Label(text=f'[size=45]{self.red1}[/size][size=40][sub]Redação 1[/sub][/size]', color=(0, 0, 0, 1),
                         font_name='Fonts/AmaticSC-Bold.ttf', markup=True)
        lbl_red2 = Label(text=f'[size=45]{self.red2}[/size][size=40][sub]Redação 2[/sub][/size]', color=(0, 0, 0, 1),
                         font_name='Fonts/AmaticSC-Bold.ttf', font_size=25, markup=True)
        lbl_red3 = Label(text=f'[size=45]{self.red3}[/size][size=40][sub]Redação 3[/sub][/size]', color=(0, 0, 0, 1),
                         font_name='Fonts/AmaticSC-Bold.ttf', font_size=25, markup=True)
        lbl_red4 = Label(text=f'[size=45]{self.red4}[/size][size=40][sub]Redação 4[/sub][/size]', color=(0, 0, 0, 1),
                         font_name='Fonts/AmaticSC-Bold.ttf', font_size=25, markup=True)
        lbl_part = Label(text=f'[size=45]{self.part}[/size][size=40][sub]Participação[/sub][/size]', color=(0, 0, 0, 1),
                         font_name='Fonts/AmaticSC-Bold.ttf', font_size=25, markup=True)
        lbl_qtd = Label(text=f'[size=45]{self.qtd}[/size][size=40][sub]Redações feitas[/sub][/size]', halign='center',
                        color=(0, 0, 0, 1), font_name='Fonts/AmaticSC-Bold.ttf', font_size=25, markup=True)
        lbl_prova = Label(text=f'[size=45]{self.prova}[/size][size=40][sub]Prova[/sub][/size]', color=(0, 0, 0, 1),
                          font_name='Fonts/AmaticSC-Bold.ttf', font_size=25, markup=True)
        lbl_rec = Label(text=f'[size=45]{self.rec}[/size][size=40][sub]Recuperação[/sub][/size]', color=(0, 0, 0, 1),
                        font_name='Fonts/AmaticSC-Bold.ttf', font_size=25, markup=True)

        labels_reds = [lbl_red1, lbl_red2, lbl_red3, lbl_red4]
        if float(self.rec) > 0:
            labels_avaliacoes = [lbl_prova, lbl_rec]
        else:
            labels_avaliacoes = [lbl_prova]
        labels_part = [lbl_part, lbl_qtd]

        for label in labels_reds:
            box_redacoes.add_widget(label)

        for label in labels_avaliacoes:
            box_avaliacoes.add_widget(label)

        for label in labels_part:
            box_avaliacoes.add_widget(label)

        if float(media) >= 7:
            aprovacao = 'APROVADO(A)'
            color = '#F24894'
        else:
            aprovacao = 'REPROVADO(A)'
            color = '#FA6900'

        titulo = Label(
            text=f'[font=Fonts/AmaticSC-Bold.ttf]{self.trimestre}º trimestre[/font]    [size=14][color={color}]{aprovacao}[/size]',
            color=(0, 0, 0, 1),
            size_hint=(1, 0.1),
            valign='middle',
            pos_hint={'center': 1},
            font_size=45,
            markup=True
            )

        self.add_widget(titulo)
        box_integral.add_widget(box_redacoes)
        box_integral.add_widget(box_avaliacoes)
        self.add_widget(box_integral)

        return self