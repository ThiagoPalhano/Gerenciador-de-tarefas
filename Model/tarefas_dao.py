import sqlite3
from typing import List, Optional, Dict

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
                    usuario_ID INTEGER NOT NULL,
                    tarefa_nome TEXT NOT NULL,
                    descricao TEXT NOT NULL,
                    data_criacao TEXT NOT NULL,
                    data_vencimento TEXT NOT NULL,
                    prioridade TEXT NOT NULL,
                    status_tarefa TEXT NOT NULL,
                    FOREIGN KEY (usuario_ID) REFERENCES usuario(id)
                )
            ''')
            conn.commit()

    def create_tarefa(self, usuario_ID: int, tarefa_nome: str, descricao: str,
                      data_criacao: str, data_vencimento: str,
                      prioridade: str, status: str) -> Optional[int]:
        with self.conn as conn:
            cursor = conn.cursor()
            cursor.execute('''
                INSERT INTO tarefas (usuario_ID, tarefa_nome, descricao, data_criacao, data_vencimento, prioridade, status_tarefa)
                VALUES (?, ?, ?, ?, ?, ?, ?)
            ''', (usuario_ID, tarefa_nome, descricao, data_criacao, data_vencimento, prioridade, status))
            conn.commit()
            return cursor.lastrowid

    def update_tarefa(self, id: int, tarefa_nome: str, descricao: str,
                      data_vencimento: str, prioridade: str, status: str):
        with self.conn as conn:
            cursor = conn.cursor()
            cursor.execute('''
                UPDATE tarefas SET
                    tarefa_nome = ?, descricao = ?, 
                    data_vencimento = ?, prioridade = ?, status_tarefa = ?
                WHERE id = ?
            ''', (tarefa_nome, descricao, data_vencimento, prioridade, status, id))
            conn.commit()

    def delete_tarefa(self, id: int):
        with self.conn as conn:
            cursor = conn.cursor()
            cursor.execute('DELETE FROM tarefas WHERE id = ?', (id,))
            conn.commit()

    def get_tarefa(self, id: int) -> Optional[Dict]:
        with self.conn as conn:
            cursor = conn.cursor()
            cursor.execute('SELECT * FROM tarefas WHERE id = ?', (id,))
            row = cursor.fetchone()
            return dict(row) if row else None

    def list_tarefas(self) -> List[Dict]:
        with self.conn as conn:
            cursor = conn.cursor()
            cursor.execute('SELECT * FROM tarefas')
            return [dict(row) for row in cursor.fetchall()]
        
    def list_tarefas_por_usuario(self, usuario_id: int) -> List[Dict]:
        with self.conn as conn:
            cursor = conn.cursor()
            cursor.execute('SELECT * FROM tarefas WHERE usuario_ID = ?', (usuario_id,))
            return [dict(row) for row in cursor.fetchall()]

    def __del__(self):
        
        self.conn.close()
