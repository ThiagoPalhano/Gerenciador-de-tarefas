import sqlite3
from datetime import datetime

def inicializar_banco():
    with sqlite3.connect('gerenciador_DAO.db') as conn:
        cursor = conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS tarefas (
               id INTEGER PRIMARY KEY AUTOINCREMENT,
               nome_tarefa TEXT NOT NULL,
               descricao TEXT NOT NULL,
               data_criacao DATETIME NOT NULL,
               data_vencimento DATETIME NOT NULL,
               prioridade TEXT NOT NULL,
               status_tarefa TEXT NOT NULL
            )
        ''')
        conn.commit()

def adicionar_tarefa(nome_tarefa, descricao, data_vencimento, prioridade, status="Pendente"):
    data_criacao = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    with sqlite3.connect('gerenciador_DAO.db') as conn:
        cursor = conn.cursor()
        cursor.execute('''
            INSERT INTO tarefas (nome_tarefa, descricao, data_criacao, data_vencimento, prioridade, status_tarefa)
            VALUES (?, ?, ?, ?, ?, ?)
        ''', (nome_tarefa, descricao, data_criacao, data_vencimento, prioridade, status))
        conn.commit()
        print(f"Tarefa '{nome_tarefa}' adicionada com sucesso!")

def deletar_tarefas(ids):
    with sqlite3.connect('gerenciador_DAO.db') as conn:
        cursor = conn.cursor()
        for id in ids:
            cursor.execute('SELECT id FROM tarefas WHERE id = ?', (id,))
            if cursor.fetchone():
                cursor.execute('DELETE FROM tarefas WHERE id = ?', (id,))
                print(f"Tarefa com ID {id} foi excluída com sucesso!")
            else:
                print(f"Nenhuma tarefa encontrada com ID {id}.")
        conn.commit()
        
def atualizar_status(id, novo_status):
    with sqlite3.connect('gerenciador_DAO.db') as conn:
        cursor = conn.cursor()
        cursor.execute('SELECT id FROM tarefas WHERE id = ?', (id,))
        if cursor.fetchone():
            cursor.execute('''
                UPDATE tarefas
                SET status_tarefa = ?
                WHERE id = ?
            ''', (novo_status, id))
            conn.commit()
            print(f"Status da tarefa ID {id} atualizado para '{novo_status}'!")
        else:
            print(f"Nenhuma tarefa encontrada com ID {id}.")

def consultar_tarefas():
    with sqlite3.connect('gerenciador_DA.db') as conn:
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM tarefas')
        tarefas = cursor.fetchall()

        if tarefas:
            print("\nLista de Tarefas:")
            print("-" * 50)
            for tarefa in tarefas:
                print(f"ID: {tarefa[0]} | Nome: {tarefa[1]} | Prioridade: {tarefa[5]} | Status: {tarefa[6]}")
        else:
            print("Nenhuma tarefa encontrada.")

def reajustar_ids():
    with sqlite3.connect('gerenciador_DAO.db') as conn:
        cursor = conn.cursor()
        cursor.execute('SELECT id FROM tarefas ORDER BY id')
        tarefas = cursor.fetchall()
        for novo_id, (antigo_id,) in enumerate(tarefas, start=1):
            cursor.execute('UPDATE tarefas SET id = ? WHERE id = ?', (novo_id, antigo_id))

        conn.commit()
        print("IDs foram reorganizados!")


inicializar_banco()

consultar_tarefas()