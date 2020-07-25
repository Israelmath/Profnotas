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


def insere_professor(professor, banco):
    conn = sqlite3.connect(join(dirname(__file__), f'{banco.title()}.db'))
    cursor = conn.cursor()

    cursor.executescript(f'''
        INSERT INTO Professor (Nome, Sobrenome, Login, Disciplina, Senha)
        VALUES ('{professor["Nome"]}', '{professor["Sobrenome"]}', '{banco.title()}','{professor["Disciplina"]}', '{professor["Senha"]}')
           
    ''')
    conn.commit()


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
            UPDATE Aluno SET (Media{qual_media}) = {float (media_valor)}
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
        INSERT INTO {"Notas"+trimestre+"tri"} (Id, '{atividade}')
        VALUES ({Id}, {Nota});
    ''')
    conn.commit()


def search_user(Identificacao, Campo_busca, banco, exato = False):
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
            SELECT * FROM '{'Notas'+trimestre+'tri'}'
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


def list_all(banco, campo = ''):
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


def turn_off(banco):
    conn = sqlite3.connect(join(dirname(__file__), f'{banco}.db'))
    conn.close()