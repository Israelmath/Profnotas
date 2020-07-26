import sqlite3
from os.path import join, dirname


def insere_aluno(Nome, Sobrenome, Turma, Serie, Numero, banco):
    conn = sqlite3.connect(join(dirname(__file__), f'{banco.title()}.db'))
    cursor = conn.cursor()
    print(f"insere aluno: {join(dirname(__file__), f'{banco.title()}.db')}")


    cursor.executescript(f'''
        INSERT INTO Aluno ( Nome, Sobrenome, Turma, Serie, Numero)
        VALUES ('{Nome}', '{Sobrenome}', '{Turma}', {Serie}, {Numero});

        INSERT INTO Notas1tri (R1) VALUES (-1);
        INSERT INTO Notas2tri (R1) VALUES (-2);
        INSERT INTO Notas3tri (R1) VALUES (-3); 
    ''')
    conn.commit()

    cursor.execute('''
        SELECT * FROM Notas1tri;    
    ''')


def atualiza_notas(notas, banco):
    conn = sqlite3.connect(join(dirname(__file__), f'{banco}.db'))

    cursor = conn.cursor()

    trimestre = f'Notas{notas["trimestre"]}tri'

    for key in notas:
        if key != 'Id' and key != 'trimestre':
            if notas[key] != '':
                if float(notas[key]) >= 0:
                    cursor.executescript(f'''
                        UPDATE {trimestre} SET ({key}) = {float(notas[key])}
                        WHERE Id = {notas['Id']}; 
                    ''')
    conn.commit()


def atualiza_medias(id, qual_media, media_valor, banco):
    if float(media_valor) >= 0:
        conn = sqlite3.connect(join(dirname(__file__), f'{banco}.db'))

        cursor = conn.cursor()

        cursor.executescript(f'''
            UPDATE Aluno SET (Media{qual_media}) = {float(media_valor)}
            WHERE Id = {id}    
        ''')
    else:
        pass


def atualiza_dados_cadastrais(aluno, banco):
    conn = sqlite3.connect(join(dirname(__file__), f'{banco}.db'))
    cursor = conn.cursor()

    for key in aluno:
        if key != 'Id':
            if aluno[key] != '-1' and aluno[key] != -1:
                cursor.executescript(f'''
                    UPDATE Aluno SET ({key}) = '{aluno[key]}'
                    WHERE Id = {aluno['Id']}; 
                ''')
    conn.commit()


def insere_nota(Id, trimestre, atividade, Nota):
    conn = sqlite3.connect(join(dirname(__file__), 'Alunos.db'))

    cursor = conn.cursor()

    cursor.execute(f'''
        INSERT INTO {"Notas" + trimestre + "tri"} (Id, '{atividade}')
        VALUES ({Id}, {Nota});
    ''')
    conn.commit()


def search_user(Identificacao, Campo_busca, banco, exato=False):
    encontrados = []
    conn = sqlite3.connect(join(dirname(__file__), f'{banco}.db'))

    cursor = conn.cursor()

    if not exato:
        cursor.execute(f'''
            SELECT * FROM Aluno
            WHERE {Campo_busca} LIKE '%{Identificacao}%' 
            OR Sobrenome LIKE '%{Identificacao}%';
        ''')
        encontrados = cursor.fetchall()
        if len(encontrados) == 0:
            print('Não encontramos nenhum(a) aluno(a)')
    else:
        cursor.execute(f'''
            SELECT * FROM Aluno
            WHERE {Campo_busca} = '{Identificacao}';
        ''')
        encontrados = cursor.fetchall()
        if len(encontrados) == 0:
            print('Não encontramos nenhum(a) aluno(a)')

    return encontrados


def busca_notas(Id, trimestre, banco):
    conn = sqlite3.connect(join(dirname(__file__), f'{banco}.db'))
    cursor = conn.cursor()

    cursor.execute(f'''
            SELECT * FROM '{'Notas' + trimestre + 'tri'}'
            WHERE Id = '{Id}';
        ''')

    return cursor.fetchall()


def del_user(Id, banco):
    conn = sqlite3.connect(join(dirname(__file__), f'{banco}.db'))
    cursor = conn.cursor()

    cursor.executescript(f'''
            DELETE FROM Aluno
            WHERE Id = '{Id}';

            DELETE FROM Notas1tri
            WHERE Id = '{Id}';

            DELETE FROM Notas2tri
            WHERE Id = '{Id}';

            DELETE FROM Notas3tri
            WHERE Id = '{Id}';
        ''')
    conn.commit()


def list_all(banco, campo=''):
    conn = sqlite3.connect(join(dirname(__file__), f'{banco}.db'))
    cursor = conn.cursor()

    if campo != '':
        cursor.execute(f'''
                SELECT {campo} FROM Aluno ORDER BY Nome;
            ''')
    else:
        cursor.execute(f'''
                SELECT * FROM Aluno ORDER BY Nome;
            ''')
    return cursor.fetchall()