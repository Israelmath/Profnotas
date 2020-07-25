import sqlite3

connection = sqlite3.connect('test.db')

cursor = connection.cursor()

cursor.execute('''CREATE TABLE IF NOT EXISTS notas(t1, t2, t3, rec)
                    VALUES 
                    (r1, r2, r3, r4),
                    (r1, r2, r3, r4),
                    (r1, r2, r3, r4),
                    (r1, r2, r3, r4)
                );''')