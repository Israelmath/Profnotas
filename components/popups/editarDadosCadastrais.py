from os.path import join, pardir

from kivy.lang import Builder
from kivy.uix.popup import Popup
import redis

from DAOs.ConfigDB import search_user, atualiza_dados_cadastrais
from components.alunoNaLista import AlunoNaLista

Builder.load_file(join(__file__, pardir, pardir, pardir, 'kvfiles/editarDadosCadastrais.kv'))

class EditarDadosCadastrais(Popup):

    def __init__(self, **kwargs):
        super().__init__()

        self.id_professor = redis.Redis().get('id_professor').decode('utf-8')
        self.id = redis.Redis().get('id_aluno').decode('utf-8')
        self.title = 'Cuidado!\nVocê está alterando informações Cadastrais'
        self.title_align = 'center'
        self.title_font = 'Fonts/AmaticSC-Bold.ttf'
        self.title_color = 0, 0, 0, 1
        self.title_size = 30
        self.background = 'white'

        self.dados_aluno = search_user(self.id, 'Id', self.id_professor, exato=True)[0]
        self.aluno_instanciado = AlunoNaLista(id=self.dados_aluno[0],
                                              nome=self.dados_aluno[1],
                                              sobrenome=self.dados_aluno[2],
                                              turma=self.dados_aluno[3].title(),
                                              serie=str(self.dados_aluno[4]),
                                              numero=str(self.dados_aluno[5]))
        self.ids.info_aluno.add_widget(self.aluno_instanciado.cria_box(pagina='Popup'))

    def insere_info(self):
        id_aluno = redis.Redis().get('id_aluno').decode('utf-8')
        id_professor = redis.Redis().get('id_professor').decode('utf-8')
        ids_pop = self.ids

        for id in ids_pop:
            if id != 'container' and id != 'info_aluno':
                if ids_pop[id].text == '':
                    ids_pop[id].text = '-1'

        dados = {'Id': id_aluno,
                 'Nome': self.ids.nome.text.title(),
                 'Sobrenome': self.ids.sobrenome.text.title(),
                 'Turma': self.ids.turma.text.title(),
                 'Serie': int(self.ids.serie.text),
                 'Numero': int(self.ids.numero.text)
                 }

        self.dismiss()
        atualiza_dados_cadastrais(dados, id_professor)