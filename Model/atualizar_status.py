import sqlite3
from datetime import datetime

def atualizar_status(tarefa_id, novo_status):
    conn = sqlite3.connect('gerenciador_DOA.db')
    cursor = conn.cursor()

    cursor.execute('''
        UPDATE tarefas
        SET status_tarefa = ?
        WHERE id = ?
    ''', (novo_status, tarefa_id))

    conn.commit()
    conn.close()
    print(f"Status da tarefa ID {tarefa_id} atualizado para '{novo_status}'!")

atualizar_status(1, "Concluído")

