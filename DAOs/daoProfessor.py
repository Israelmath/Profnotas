import sqlite3
from os.path import join, dirname


def insere_professor(professor, banco):
    conn = sqlite3.connect(join(dirname(__file__), f'{banco.title()}.db'))
    cursor = conn.cursor()

    cursor.executescript(f'''
        INSERT INTO Professor (Nome, Sobrenome, Login, Disciplina, Senha)
        VALUES ('{professor["Nome"]}', '{professor["Sobrenome"]}', '{banco.title()}','{professor["Disciplina"]}', '{professor["Senha"]}')

    ''')
    conn.commit()