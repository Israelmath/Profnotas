from kivy.app import App
from kivy.uix.image import Image
from kivy.uix.screenmanager import ScreenManager
from kivy.uix.button import Button
from Screens.loginTela import LoginTela
from Screens.calendarioTela import CalendarioTela
from Screens.adicionaAlunoTela import AdicionaAlunoTela
from models.formAluno import FormAluno
from Screens.listarAlunoTela import ListarAlunoTela
from Relatorio import CriarRelatorio
from DAOs.ConfigDB import *
from components.popups.editarDadosCadastrais import EditarDadosCadastrais
from components.popups.inserirDados import InserirDados
from kivy.lang.builder import Builder
from Screens.buscaAlunoTela import BuscaAlunoTela
from auxiliarClasses.auxiliar import *
from Screens.mainMenu import MenuPrincipal
from Screens.infoTela import InfoTela
from models.alunos import Aluno
from models.professor import Professor
from Screens.criarUsuarioTela import CriarUsuarioTela
from components.botaoMenu import BotaoMenu
import redis

Builder.load_file(join(dirname(__file__), 'kvfiles/profnotas.kv'))


class Gerenciador(ScreenManager):

    def open_popup_inserirnotas(self):
        InserirDados().open()

    def open_popup_EditarDadosCadastrais(self):
        EditarDadosCadastrais().open()

    def criar_relatorio(self, *args):
        id_professor = redis.Redis().get('id_professor').decode('utf-8')
        id_aluno = redis.Redis().get('id_aluno').decode('utf-8')

        if int(id_aluno) > 0:
            relatorio = CriarRelatorio(id_aluno, id_professor)
            relatorio.cria_relatorio()


class ProfNotasApp(App):
    title = 'ProfNotas'


    def build(self):
        professor = Professor()
        aluno = Aluno()
        professor.nome = 'admin'
        aluno.numero = 0

        return Gerenciador()


if __name__ == '__main__':
    ProfNotasApp().run()
