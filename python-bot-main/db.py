import sqlite3

conn = sqlite3.connect('db1.db')
cursor = conn.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS "Group" (
    id INTEGER PRIMARY KEY,
    name TEXT 
)
''')

cursor.execute('''
CREATE TABLE IF NOT EXISTS Student (
    id INTEGER PRIMARY KEY,
    f TEXT,
    i TEXT,
    o TEXT,
    groupid INTEGER,
    FOREIGN KEY (groupid) REFERENCES "Group"(id)
)
''')

cursor.execute('''
INSERT INTO "Group" (id, name) VALUES
(1, '215 группе'),
(2, '217 группе'),
(3, '218 группе'), 
(4, '219 группе'),
(5, '220 группе'); 

''')

cursor.execute('''
INSERT INTO Student (id, f, i, o, groupid) VALUES
(1, 'Ларионов', 'Алекс', 'Сергеевич', 1),
(2, 'Скворкин', 'Кирилл', 'Алексеевич', 2),
(3, 'Скворкин', 'Кирилл', 'Алексеевич', 3),
(4, 'Петров', 'Кирилл', 'Алексеевич', 4),
(5, 'Давлетов', 'Кирилл', 'Алексеевич', 5);

''')

conn.commit()
conn.close()
