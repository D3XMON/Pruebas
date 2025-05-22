import sqlite3

conn = sqlite3.connect('usuarios.db')
cursor = conn.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS usuarios (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    usuario TEXT UNIQUE NOT NULL,
    contraseña TEXT NOT NULL
)
''')

# Insertar usuarios de ejemplo (evita repetirlos)
usuarios = [
    ('sebastian', '1234'),
    ('maria', 'abcd'),
    ('juan', 'pass123')
]

for u, p in usuarios:
    try:
        cursor.execute('INSERT INTO usuarios (usuario, contraseña) VALUES (?, ?)', (u, p))
    except sqlite3.IntegrityError:
        pass

conn.commit()
conn.close()
