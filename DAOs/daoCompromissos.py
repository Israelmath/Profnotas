import sqlite3
from os.path import join, dirname


def salva_compromisso(compromisso, banco):
    conn = sqlite3.connect(join(dirname(__file__), f'{banco.title()}.db'))
    cursor = conn.cursor()

    cursor.executescript(f'''
        INSERT INTO Anotacoes (Titulo, Data_anotacao, Anotacao, Cor)
        VALUES ('{compromisso["Titulo"]}', '{compromisso["Data"]}', '{compromisso["Anotacao"]}', '{compromisso["Cor"]}')
    ''')

    conn.commit()

def busca_compromisso(banco):
    conn = sqlite3.connect(join(dirname(__file__), f'{banco.title()}.db'))
    cursor = conn.cursor()

    cursor.execute(f'''
        SELECT * FROM Anotacoes;
    ''')

    return cursor.fetchall()