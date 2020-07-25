#!/usr/bin/python
"""
This example shows how multirow and multicolumns can be used.
..  :copyright: (c) 2014 by Jelte Fennema.
    :license: MIT, see License for more details.
"""

# begin-doc-include
from pylatex import Document, Section, Subsection, Tabular, MultiColumn, \
    Command, NoEscape, Tabularx, MiniPage, StandAloneGraphic
from pylatex.utils import bold
from pylatex.basic import NewLine, LargeText
from numpy import mean
from DAOs.ConfigDB import search_user, busca_notas, list_all
from Graphs import Graficos


class CriarRelatorio():

    def __init__(self, id, banco, *args):
        self.id = id
        self.banco = banco
        self.resumo = search_user(id, 'Id', self.banco)[0]
        self.notas = self.busca_notas(id)
        self.path_graf_medias = self.cria_grafico()
        self.path_graf_1tri = self.cria_grafico(trimestre = '1')
        self.path_graf_2tri = self.cria_grafico(trimestre = '2')
        self.path_graf_3tri = self.cria_grafico(trimestre = '3')
        self.path_graf_geral = ''
        self.alunos_ids = list_all(self.banco, 'Id')

    def busca_notas(self, id):
        notas = []
        for t in range(3):
            notas.append(busca_notas(id, str(t+1), self.banco)[0])
        return(notas)

    def cria_grafico(self, dados = '', trimestre = ''):

        if trimestre == '1':
            notas = self.notas[0]
            graficos = Graficos(medias = notas[1:5], periodo = trimestre)
        elif trimestre == '2':
            notas = self.notas[1]
            graficos = Graficos(medias = notas[1:5], periodo = trimestre)
        elif trimestre == '3':
            notas = self.notas[2]
            graficos = Graficos(medias = notas[1:5], periodo = trimestre)
        else:
            notas = self.resumo
            graficos = Graficos(medias = notas[6:9])
        
        return graficos.grafico_barra(path = True)

    def cria_grafico_com_marcadores(self, dados, marcadores):
        grafico = Graficos(medias = dados)
        return grafico.graficos_relatorio(marcadores, path = True)

    def cria_primeira_secao(self, cabecalho):
        colunas_section_1 = Tabularx('c c c')
        colunas_section_1.add_row([MultiColumn(3, align = 'c')])

        info_aluno = MiniPage(width = NoEscape(r'0.25\textwidth'), pos = 'b', align = 'l')
        graf_media = StandAloneGraphic(filename = self.path_graf_medias, image_options = 'width = 180 px')
        box_medias_aluno = MiniPage(width = NoEscape(r'0.23\textwidth'), pos = 'b', align = 'l')
        
        info_aluno.append(f'Nome: {self.resumo[1]} {self.resumo[2]}')
        info_aluno.append(NewLine())
        info_aluno.append(f'Número: {self.resumo[5]}')
        info_aluno.append(NewLine())
        info_aluno.append(f'Série: {self.resumo[4]}º ano')
        info_aluno.append(NewLine())
        info_aluno.append(f'Turma: {self.resumo[3]}')
        info_aluno.append(NewLine())
        info_aluno.append(NewLine())
        if self.resumo[9] >= 45:
            info_aluno.append(LargeText(f'Aprovado'))
        else:
            info_aluno.append(LargeText(f'Reprovado'))
        
        for i in range(3):
            info_aluno.append(NewLine())
        

        media_final = LargeText(f'Média final: {self.resumo[9]}')
        info_aluno_medias = Tabular('c | c | c', pos = 'b')
        info_aluno_medias.add_row(cabecalho, mapper = [bold])
        info_aluno_medias.add_hline()
        info_aluno_medias.add_empty_row()
        info_aluno_medias.add_row([self.resumo[6], self.resumo[7], self.resumo[8]])

        box_medias_aluno.append(media_final)
        for i in range(3):
            box_medias_aluno.append(NewLine())

        box_medias_aluno.append(info_aluno_medias)  
        for i in range(3):
            box_medias_aluno.append(NewLine())

        colunas_section_1.add_row([info_aluno, graf_media, box_medias_aluno])
        
        return colunas_section_1

    def cria_subsecao(self, cabecalho, tri):
        
        notas = []
        for n in range(4):
            if self.notas[tri][n+1] < 0:
                notas.append(0)
            else:
                notas.append(self.notas[tri][n+1])

        colunas_subsection_1 = Tabular('c c')
        colunas_subsection_1.add_row([MultiColumn(2, align = 'c')])

        if tri == 0:
            graf_1tri = StandAloneGraphic(filename = self.path_graf_1tri, image_options = 'width = 190 px')
        elif tri == 1:
            graf_1tri = StandAloneGraphic(filename = self.path_graf_2tri, image_options = 'width = 190 px')
        elif tri == 2:
            graf_1tri = StandAloneGraphic(filename = self.path_graf_3tri, image_options = 'width = 190 px')

        box_1tri = MiniPage(width = NoEscape(r'0.49\textwidth'), pos='b')
        
        info_aluno_1tri = Tabular('c | c | c | c', pos = 'b')
        info_aluno_1tri.add_row(cabecalho, mapper = [bold])
        info_aluno_1tri.add_hline()
        info_aluno_1tri.add_empty_row()
        
        info_aluno_1tri.add_row([notas[0], notas[1], notas[2], notas[3]])
        
        box_1tri.append(info_aluno_1tri)
        box_1tri.append(NewLine())
        box_1tri.append(NewLine())
        box_1tri.append('*As notas das redações estão entre 0 e 8')
        for i in range(3):
            box_1tri.append(NewLine())
        
        colunas_subsection_1.add_row([graf_1tri, box_1tri])    
        
        return colunas_subsection_1

    def cria_segunda_secao(self):
        redacoes_notas = {'1ª Redação': [],
                          '2ª Redação': [],
                          '3ª Redação': [],
                          '4ª Redação': [], 
                          'Médias': True}
        
        path_graf_gerais = []
        graficos_gerais = []
        table_sup = Tabular('c c')
        table_inf = Tabular('c c')
        table_sup.add_row([MultiColumn(2, align = 'c')])
        table_inf.add_row([MultiColumn(2, align = 'c')])

        for i in range(3):
            # print(self.notas)
            marcadores = list(self.notas[i][1:5])
            if marcadores[i] < 0:
                marcadores[i] = 0
            print(marcadores)
    
            for aluno in self.alunos_ids:
                notas = busca_notas(aluno[0], str(i+1), self.banco)[0][1:5]
                redacoes_notas['1ª Redação'].append(notas[0])
                redacoes_notas['2ª Redação'].append(notas[1])
                redacoes_notas['3ª Redação'].append(notas[2])
                redacoes_notas['4ª Redação'].append(notas[3])

            for red in redacoes_notas:
                redacoes_notas[red] = [mean(redacoes_notas[red]).round(2)]
                if redacoes_notas[red][0] < 0:
                    redacoes_notas[red][0] = 0

            path_graf_gerais.append(self.cria_grafico_com_marcadores(dados = redacoes_notas, marcadores = marcadores))

        for g in path_graf_gerais:
            graficos_gerais.append(StandAloneGraphic(filename = g, image_options = 'width = 190 px'))
        
        table_sup.add_row([graficos_gerais[0], graficos_gerais[1]])
        table_inf.add_row([graficos_gerais[2], graficos_gerais[2]])

        # graf_comparacao_1 = StandAloneGraphic(filename = path_graf_gerais[0], image_options = 'width = 190 px')

        return [table_sup, table_inf]
    
    def cria_relatorio(self):
        margens = {'margin': '1.5cm', 'tmargin': '1cm'}
        doc = Document(f'Relatórios/{self.resumo[1]} {self.resumo[2]}', geometry_options = margens, page_numbers = False)

        # Definindo marcações e cabeçalhos
        cabecalho_trimestre = ['1ª redação', '2ª redação', '3ª redação', '4ª redação']
        cabecalho_ano = ['Média 1º tri', 'Média 2º tri', 'Média 3º tri']
    
        doc.preamble.append(Command('title', 'Relatório escolar'))
        doc.preamble.append(Command('author', 'Profª Joice da Silva Moreli'))
        doc.append(NoEscape(r'\maketitle'))

        # Definindo Seções e Subseções
        section_1 = Section('Informações do aluno:', numbering = False)
        section_2 = Section('Comparação com todos os alunos:', numbering = False)

        subsec_1tri = Subsection('1º Trimestre:', numbering = False)
        subsec_2tri = Subsection('2º Trimestre:', numbering = False)
        subsec_3tri = Subsection('3º Trimestre:', numbering = False)

        # Criando conteúdo da primeira seção
        primeira_secao = self.cria_primeira_secao(cabecalho_ano)

        # Criando conteúdo da primeira subseção
        subsec_1tri.append(self.cria_subsecao(cabecalho = cabecalho_trimestre, tri = 0))        
        
        # Criando conteúdo da segunda subseção
        subsec_2tri.append(self.cria_subsecao(cabecalho = cabecalho_trimestre, tri = 1))

        # Criando conteúdo da terceira subseção
        subsec_3tri.append(self.cria_subsecao(cabecalho = cabecalho_trimestre, tri = 2))

        # Criando conteúdo para segunda seção
        rows_segunda_secao = self.cria_segunda_secao()
        
        
        # Adicionando coluna e subseções à primeira seção
        section_1.append(primeira_secao)
        for row in reversed(rows_segunda_secao):
            section_2.append(row)
            section_2.append(NewLine())
        section_1.append(subsec_1tri)
        section_1.append(subsec_2tri)
        section_1.append(subsec_3tri)


        doc.append(section_1)
        doc.append(section_2)


        doc.generate_pdf(f'Relatórios/{self.resumo[1].strip()} {self.resumo[2].strip()}', clean_tex=False)

if __name__ == '__main__':
    relatorio = CriarRelatorio(2, 'Israel')
    relatorio.cria_relatorio()