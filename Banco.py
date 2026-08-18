import sqlite3

banco_de_dados = sqlite3.connect('banco.db')
cursor = banco_de_dados.cursor()
cursor.execute('''
CREATE TABLE IF NOT EXISTS dados (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    dados TEXT NOT NULL,
)
''')

banco_de_dados.commit()
