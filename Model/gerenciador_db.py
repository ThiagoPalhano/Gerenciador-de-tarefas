import sqlite3

conn=sqlite3.Connection("gerenciador_de_tarefas.db")
cur=conn.cursor()

cur.execute('''
    CREATE TABLE IF NOT EXISTS usuario (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL,
        idade INTEGER,
        email TEXT UNIQUE
    )
''')

cur.execute('''
    CREATE TABLE IF NOT EXISTS tarefas (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        usuario_id INTEGER,
        nome_tarefa TEXT NOT NULL,
        descricao TEXT NOT NUll,
        data_criacao DATETIME,
        data_vencimento DATETIME,
        prioridade TEXT NOT NULL,
        status_tarefa TEXT NOT NULL,
        FOREIGN KEY(usuario_id) REFERENCES usuario(id)
    )
''')

conn.commit()
conn.close()




