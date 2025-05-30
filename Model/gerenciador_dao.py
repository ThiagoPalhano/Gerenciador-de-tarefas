import sqlite3
from typing import List, Optional


class GerenciadorDao:
    def __init__(self, dbpath: str):
        self.conn = sqlite3.connect(dbpath)
        self.conn.row_factory = sqlite3.Row
        self._create_table()

    def _create_table(self):
        with self.conn as conn:
            cursor = conn.cursor()
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS tarefas (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    usuario_id INTEGER,
                    tarefa_nome TEXT NOT NULL,
                    descricao TEXT NOT NULL,
                    data_criacao TEXT NOT NULL,
                    data_vencimento TEXT NOT NULL,
                    prioridade TEXT NOT NULL,
                    status_tarefa TEXT NOT NULL
                )
            ''')
            conn.commit()

    def create_tarefa(self, usuario_id: int, tarefa_nome: str, descricao: str,
                      data_criacao: str, data_vencimento: str,
                      prioridade: str, status: str) -> int:
        with self.conn as conn:
            cursor = conn.cursor()
            cursor.execute('''
                INSERT INTO tarefas (usuario_id, tarefa_nome, descricao, data_criacao, data_vencimento, prioridade, status_tarefa)
                VALUES (?, ?, ?, ?, ?, ?, ?)
            ''', (usuario_id, tarefa_nome, descricao, data_criacao, data_vencimento, prioridade, status))
            conn.commit()
            return cursor.lastrowid

    def update_tarefa(self, id: int, usuario_id: int, tarefa_nome: str, descricao: str,
                      data_criacao: str, data_vencimento: str,
                      prioridade: str, status: str):
        with self.conn as conn:
            cursor = conn.cursor()
            cursor.execute('''
                UPDATE tarefas SET
                    usuario_id = ?, tarefa_nome = ?, descricao = ?, data_criacao = ?, 
                    data_vencimento = ?, prioridade = ?, status_tarefa = ?
                WHERE id = ?
            ''', (usuario_id, tarefa_nome, descricao, data_criacao, data_vencimento, prioridade, status, id))
            conn.commit()

    def delete_tarefa(self, id: int):
        with self.conn as conn:
            cursor = conn.cursor()
            cursor.execute('DELETE FROM tarefas WHERE id = ?', (id,))
            conn.commit()

    def get_tarefa(self, id: int) -> Optional[sqlite3.Row]:
        with self.conn as conn:
            cursor = conn.cursor()
            cursor.execute('SELECT * FROM tarefas WHERE id = ?', (id,))
            return cursor.fetchone()

    def list_tarefas(self) -> List[sqlite3.Row]:
        with self.conn as conn:
            cursor = conn.cursor()
            cursor.execute('SELECT * FROM tarefas')
            return cursor.fetchall()

    def __del__(self):
        self.conn.close()
