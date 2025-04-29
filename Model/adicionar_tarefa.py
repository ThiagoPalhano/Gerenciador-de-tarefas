import sqlite3
from datetime import datetime


def adicionar_tarefa(titulo, descricao, data_vencimento, prioridade, status="Pendente"):

    conn = sqlite3.connect('gerenciador_DOA.db')  
    cursor = conn.cursor()

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS tarefas (
           id INTEGER PRIMARY KEY AUTOINCREMENT,
           nome_tarefa TEXT NOT NULL,
           descricao TEXT NOT NULL,
           data_criacao DATETIME,
           data_vencimento DATETIME,
           prioridade TEXT NOT NULL,
           status_tarefa TEXT NOT NULL
        )
    ''')

    data_criacao = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
   
    cursor.execute('''
        INSERT INTO tarefas (nome_tarefa, descricao, data_criacao, data_vencimento, prioridade, status_tarefa)
        VALUES (?, ?, ?, ?, ?, ?)
    ''', (titulo, descricao, data_criacao, data_vencimento, prioridade, status))


    conn.commit()
    conn.close()
    print(f"Tarefa '{titulo}' adicionada com sucesso!")


adicionar_tarefa(
    titulo="Estudar Python",
    descricao="Praticar criação de gerenciadores de tarefas",
    data_vencimento="2025-04-30",
    prioridade="Alta",
    status="Agendada"
)

adicionar_tarefa(
    titulo="Reunião com Paulo",
    descricao="Discutir progresso do projeto",
    data_vencimento="2025-04-29",
    prioridade="Média",
    status="Agendada"
)
