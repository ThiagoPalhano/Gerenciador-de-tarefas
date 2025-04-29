import sqlite3

def consultar_tarefas():
    conn = sqlite3.connect('gerenciador_DOA.db')
    cursor = conn.cursor()

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS tarefas (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome_tarefa TEXT NOT NULL,
            descricao TEXT,
            data_criacao DATETIME,
            data_vencimento DATETIME,
            prioridade TEXT NOT NULL,
            status_tarefa TEXT NOT NULL
        )
    ''')

    cursor.execute('SELECT * FROM tarefas')
    tarefas = cursor.fetchall()

    if tarefas:
        for tarefa in tarefas:
            print(tarefa)
    else:
        print("Nenhuma tarefa encontrada.")

    conn.close()

consultar_tarefas()