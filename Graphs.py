from os import remove, mkdir, listdir
from os.path import dirname, join
import matplotlib.pyplot as plt
import seaborn as sns
from collections import Counter
from kivy.uix.image import Image
import pandas as pd
from numpy import mean, round
from random import randint

class Graficos():


    def __init__(self, medias = [], periodo = '', imagem = ''):
        self.imagem = imagem
        self.marcadores = []
        self.grafico_titulo = self.titulo(medias, periodo)
        self.data = self.trata_dados(medias, periodo)
        if 'Médias' in self.grafico_titulo:
            self.axis = [-0.5, len(medias)-0.5, 0, 10]
        else:
            self.axis = [-0.5, len(medias)-0.5, 0, 8.5]


    def titulo(self, medias, periodo):
        if len(medias) == 3:
            return 'Médias de cada trimestre'
        else:
            if isinstance(medias, dict) and 'Médias' in medias:
                del medias['Médias']
                return f'Médias por redação'
            else:
                return f'Redações do {periodo}º trimestre'


    def trata_dados(self, medias, periodo):

        if isinstance(medias, list) or isinstance(medias, tuple):
            df = pd.DataFrame()

            medias = [float(medias[i]) for i in range(len(medias))]
        
            if max(medias) < 0:
                medias = [0] * len(medias)

            if len(medias) == 3:
                for i in range(3):
                    if medias[i] < 0:
                        self.marcadores.append(0)
                        df[f'{str(i+1)}º Trimestre'] = [0]
                    else:
                        self.marcadores.append(medias[i])
                        df[f'{str(i+1)}º Trimestre'] = [medias[i]]
                
            
            elif len(medias) == 4:
                for i in range(4):
                    if medias[i] < 0:
                        self.marcadores.append(0)
                        df[f'Redação {str(i+1)}'] = [0]
                    else:
                        self.marcadores.append(medias[i])
                        df[f'Redação {str(i+1)}'] = [medias[i]]

        elif isinstance(medias, dict):
            for m in medias:
                self.marcadores.append(medias[m][0])
            
            df = pd.DataFrame(medias)
        
        return df


    def grafico_barra(self, path = False):
        key = str(randint(1, 100))
        self.imagem = sns.barplot(data = self.data, palette = 'pastel')
        self.imagem.set_title(self.grafico_titulo, fontsize = 20)
        self.imagem.axis(self.axis)
        plt.plot(self.data.columns, self.marcadores, marker = 'o', color = 'black', linestyle = '-')
        plt.savefig(join(dirname(__file__), 'Estatistica/temporario'+key+'.png'))
        plt.clf()
        if not path:
            return Image(source = 'Estatistica/temporario'+key+'.png', size_hint = (1,1))
        else:
            return join(dirname(__file__), 'Estatistica/temporario'+key+'.png')


    def graficos_relatorio(self, marcadores, path = False):
        key = str(randint(1, 100))
        plt.title(self.grafico_titulo, fontsize = 20)
        self.imagem = sns.barplot(data = self.data, palette = 'pastel')
        self.imagem.axis([-0.5, 3.5, 0, 8.5])
        plt.plot(self.data.columns, marcadores, marker = 'o', color = 'black', linestyle = '-')
        plt.savefig(join(dirname(__file__), 'Estatistica/temporario'+key+'.png'))
        plt.clf()
        if not path:
            return Image(source = 'Estatistica/temporario'+key+'.png', size_hint = (1,1))
        else:
            return join(dirname(__file__), 'Estatistica/temporario'+key+'.png')

        
    def deleta_graficos(self, excessao = []):
        graficos_salvos = listdir(join(dirname(__file__), 'Estatistica'))
        for g in graficos_salvos:
            if g.endswith('.jpg') or g.endswith('.png'):
                remove(join(dirname(__file__),'Estatistica/'+g))


if __name__ == '__main__':
    teste = redacoes_notas = {'1ª Redação': [3],
                              '2ª Redação': [6],
                              '3ª Redação': [7],
                              '4ª Redação': [8]}
    marks = [3,2,3,6]
    graf = Graficos(medias = teste)
    graf.graficos_relatorio(marcadores = marks)

