from datetime import datetime
from kivy.uix.popup import Popup
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.image import Image
from kivy.uix.screenmanager import Screen

def adiciona_aluno(choice):
    if choice == '1':
        return True
    else:
        return False


def mostra_cadastro(choice):
    if choice == '2':
        return True
    else:
        return False


def escolha_aluno(choice):
    if choice == '3':
        return True
    else:
        return False


def exclui_usuario(choice):
    if choice == '4':
        return True
    else:
        return False


def certifica_nome(nome):
    if nome.isalpha():
        return True
    else:
        print('\033[36mUsuário não pôde ser cadastrado. Nome inválido.\033[m')
        return False


def certifica_serie(numero):
    print(numero, type(numero), len(numero))
    if len(numero) != 1 and len(numero) != 2:
        print('\033[36mNúmero errado ou código de área faltante.\033[m')
        return False
    else:
        return True

def verifica_senha(senha):
    if int(senha) == datetime.today().hour:
        return True
    else:
        return False


def verifica_exclusao(from_layout = False):
    if not from_layout:
        print('Você realmente deseja excluir o(a) aluno(a)? (S/n)')
        if input().lower() == 's':
            senha = input('Digite sua senha: ')
            if verifica_senha(senha):
                return True
            else:
                return False
        else:
            return False
    else:
        return True

def calcula_media_trimestral(R1, R2, R3, R4, Qtd, Prova, Rec):
    qtd_de_redacoes = 4
    r1 = float(R1)
    r2 = float(R2)
    r3 = float(R3)
    r4 = float(R4)
    prova = float(Prova)
    rec = float(Rec)
    qtd_parcial = int(Qtd)
    qtd_total = 0
    if qtd_parcial <= 0:
        qtd_parcial = 1
    elif qtd_parcial > 4:
        qtd_total = qtd_parcial
        qtd_parcial = 4
    media_mensal = 0
    if r1 < 0:
        r1 = 0
    if r2 < 0:
        r2 = 0
    if r3 < 0:
        r3 = 0
    if r4 < 0:
        r4 = 0
    if prova < 0:
        prova = 0

    media_mensal = (r1 + r2 + r3 + r4)/qtd_parcial
    
    
    participacao = round(qtd_parcial/qtd_de_redacoes, 2) * 2
    
    if r1 <= 0 and r2 <= 0 and r3 <= 0 and r4 <= 0:
        media_trimestral = 0
    else:
        media_trimestral = ((media_mensal + participacao) + 2*prova)/3
        
    
    return str(round(media_trimestral, 2))

def media_final(medias_trimestrais):
    if len(medias_trimestrais) < 3:
        print('Erro na qtd de médias trimestrais')
        return 0
    else:
        medias = [float(medias_trimestrais[i])*(i+1) for i in range(len(medias_trimestrais))]
        return round(sum(medias))

if __name__ == "__main__":
    pass
