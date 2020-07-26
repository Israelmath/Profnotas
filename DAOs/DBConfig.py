import sqlite3
from os.path import join, dirname
from os import listdir
import redis


def inicia_banco(banco):

    conn = sqlite3.connect(join(dirname(__file__), f'{banco.title()}.db'))
    cursor = conn.cursor()

    cursor.executescript('''
        CREATE TABLE IF NOT EXISTS Notas1tri(
            Id INTEGER PRIMARY KEY AUTOINCREMENT,
            R1 FLOAT DEFAULT -1,
            R2 FLOAT DEFAULT -1,
            R3 FLOAT DEFAULT -1,
            R4 FLOAT DEFAULT -1,
            Participacao FLOAT DEFAULT -1,
            Qtd INT DEFAULT 0,
            Prova FLOAT DEFAULT -1,
            Rec FLOAT DEFAULT -1
            );
        
        CREATE TABLE IF NOT EXISTS Notas2tri(
            Id INTEGER PRIMARY KEY AUTOINCREMENT,
            R1 FLOAT DEFAULT -2,
            R2 FLOAT DEFAULT -2,
            R3 FLOAT DEFAULT -2,
            R4 FLOAT DEFAULT -2,
            Participacao FLOAT DEFAULT -2,
            Qtd INT DEFAULT 0,
            Prova FLOAT DEFAULT -2,
            Rec FLOAT DEFAULT -2
            );
            
        CREATE TABLE IF NOT EXISTS Notas3tri(
            Id INTEGER PRIMARY KEY AUTOINCREMENT,
            R1 FLOAT DEFAULT -3,
            R2 FLOAT DEFAULT -3,
            R3 FLOAT DEFAULT -3,
            R4 FLOAT DEFAULT -3,
            Participacao FLOAT DEFAULT -3,
            Qtd INT DEFAULT 0,
            Prova FLOAT DEFAULT -3,
            Rec FLOAT DEFAULT -3
            );
            
        CREATE TABLE IF NOT EXISTS Aluno(
            Id INTEGER PRIMARY KEY AUTOINCREMENT,
            Nome VARCHAR(45) NULL,
            Sobrenome VARCHAR(45) NULL,
            Turma VARCHAR(1) NULL,
            Serie TINYINT(1) NULL,
            Numero TINYINT(3) NULL,
            Media1 FLOAT DEFAULT 0,
            Media2 FLOAT DEFAULT 0,
            Media3 FLOAT DEFAULT 0,
            MediaF FLOAT DEFAULT 0
            );

        CREATE TABLE IF NOT EXISTS Professor(
            Id INTEGER PRIMARY KEY AUTOINCREMENT,
            Nome VARCHAR(45) NOT NULL,
            Sobrenome VARCHAR(45) NULL,
            Login VARCHAR(45) NULL,
            Disciplina VARCHAR(30) NOT NULL,
            Senha NVARCHAR(30) NOT NULL            
        );

        CREATE TABLE IF NOT EXISTS Anotacoes(
            Id INTEGER PRIMARY KEY AUTOINCREMENT,
            Titulo VARCHAR(45) NOT NULL,
            Anotacao VARCHAR(5000) NOT NULL,
            Data_anotacao DATE NOT NULL,
            Inicio TIME NULL, 
            Termino TIME NULL,
            Cor VARCHAR(20) NULL
        );
    ''')


def busca_banco(banco):
    current_dir = listdir(dirname(__file__))
    for path in current_dir:
        if path.endswith('.db'):
            if path[:len(path)-3] == banco:
                return True
    
    return False


def busca_info(banco, senha = False):
    conn = sqlite3.connect(join(dirname(__file__), f'{banco}.db'))
    cursor = conn.cursor()

    if senha:
        cursor.execute(f'''
                SELECT Senha FROM Professor;
            ''')
    else:
        cursor.execute(f'''
                SELECT * FROM Professor;
            ''')

    return cursor.fetchall()[0]





def turn_off(banco):
    conn = sqlite3.connect(join(dirname(__file__), f'{banco}.db'))
    conn.close()