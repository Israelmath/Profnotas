from os import pardir
from os.path import join

from kivy.lang import Builder
from kivy.uix.screenmanager import Screen
import redis

import Graphs
from DAOs.ConfigDB import busca_notas, search_user, atualiza_medias
from Verificadores import calcula_media_trimestral, media_final
from auxiliarClasses.auxiliar import AlterarGraphBubble
from components.boxMedias import BoxMedias
from components.boxResumo import BoxResumo
from components.notasAluno import NotasAluno

Builder.load_file(join(__file__, pardir, pardir, 'kvfiles/infoTela.kv'))

class InfoTela(Screen):

    def __init__(self, **kw):
        super().__init__()
        self.inst_screen = ''
        self.id_professor = redis.Redis().get('id_professor').decode('utf-8')

    def on_pre_enter(self, *args):
        ids_tela = self.ids.values()
        for id in ids_tela:
            id.clear_widgets()
        self.update()

    def cria_grafico(self, medias, tipo='barra', info='medias'):
        Graphs.Graficos.deleta_graficos(self)
        if tipo == 'barra':
            graph = Graphs.Graficos(medias, periodo=info)
            grafico_medias = graph.grafico_barra()
            self.ids.grafico.add_widget(grafico_medias)

    def seleciona_informacoes(self, medias=[], tipo='barra', info='medias'):
        id_aluno = redis.Redis().get('id_aluno').decode('utf-8')
        id_professor = redis.Redis().get('id_professor').decode('utf-8')
        tipo_final = tipo

        if info != 'medias':
            medias = list(busca_notas(id_aluno, info, id_professor)[0])
            medias = medias[1:5]
            self.ids.grafico.clear_widgets()
            Graphs.Graficos.deleta_graficos(self)
            self.cria_grafico(medias, info=info)
        else:
            self.cria_grafico(medias, tipo=tipo_final, info=info)

    def bubble(self, inst):
        bolha = AlterarGraphBubble()
        inst.add_widget(bolha)
        self.inst_screen = inst

    def dismiss_bubble(self, inst):
        self.remove_widget(inst)

    def just_update(self, *args):
        self.update(just_entered=False)

    def on_leave(self, *args):
        Graphs.Graficos.deleta_graficos(self)

    def cria_box_notas(self):
        id_aluno = redis.Redis().get('id_aluno').decode('utf-8')
        id_professor = redis.Redis().get('id_professor').decode('utf-8')

        trimestre = 0
        notas_por_trimestre = []
        inst_notas = []

        for i in range(1, 4):
            notas_encontradas = busca_notas(id_aluno, str(i), id_professor)[0]
            notas_por_trimestre.append(notas_encontradas)

        for notas in notas_por_trimestre:
            trimestre += 1
            aluno = NotasAluno(id=notas[0],
                               trimestre=trimestre,
                               red1=notas[1],
                               red2=notas[2],
                               red3=notas[3],
                               red4=notas[4],
                               part=notas[5],
                               qtd=notas[6],
                               prova=notas[7],
                               rec=notas[8])
            inst_notas.append(aluno.cria_box())

        return inst_notas

    def update(self, just_entered=True, *args):
        id_aluno = redis.Redis().get('id_aluno').decode('utf-8')
        id_professor = redis.Redis().get('id_professor').decode('utf-8')

        # Limpa tela
        if not just_entered:
            ids_tela = self.ids.values()
            for id in ids_tela:
                id.clear_widgets()

        inst_AlunoNotas = self.cria_box_notas()

        aluno_resumo = search_user(id_aluno, 'Id', banco= id_professor)
        medias = []
        for notas in inst_AlunoNotas:
            self.ids.integral.add_widget(notas)
            medias.append(calcula_media_trimestral(R1=notas.red1,
                                                   R2=notas.red2,
                                                   R3=notas.red3,
                                                   R4=notas.red4,
                                                   Qtd=notas.qtd,
                                                   Prova=notas.prova,
                                                   Rec=notas.rec))

        box_das_medias = BoxMedias(media1=medias[0],
                                   media2=medias[1],
                                   media3=medias[2],
                                   mediaf=str(media_final(medias[:4]))
                                   )

        for i in range(len(medias) + 1):
            if i == len(medias):
                atualiza_medias(id_aluno, 'f', media_final(medias[:4]), id_professor)
            else:
                atualiza_medias(id_aluno, i + 1, medias[i], id_professor)

        self.ids.medias.add_widget(box_das_medias.cria_box())
        if len(aluno_resumo) > 0:
            aluno = aluno_resumo[0]
            info_aluno = BoxResumo(id=aluno[0],
                                   nome=aluno[1],
                                   sobrenome=aluno[2],
                                   turma=aluno[3].title(),
                                   serie=str(aluno[4]),
                                   numero=str(aluno[5])
                                   )
            box_aluno = info_aluno.cria_box()
            self.ids.resumo.add_widget(box_aluno)

            self.seleciona_informacoes(medias)