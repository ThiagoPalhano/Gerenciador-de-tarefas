import sqlite3
from typing import List, Optional, Dict

class UsuarioDao:
    def __init__(self, dbpath: str):
        self.conn = sqlite3.connect(dbpath)
        self.conn.row_factory = sqlite3.Row

        with self.conn as conn:
            cursor = conn.cursor()
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS usuario (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    nome TEXT NOT NULL,
                    idade INTEGER,
                    email TEXT UNIQUE
                )
            ''')
            conn.commit()

    def add_usuario(self, nome: str, idade: Optional[int], email: str) -> str:
        with self.conn as conn:
            cursor = conn.cursor()
            try:
                cursor.execute('''
                    INSERT INTO usuario (nome, idade, email)
                    VALUES (?, ?, ?)
                ''', (nome, idade, email))
                conn.commit()
                user_id = cursor.lastrowid
                return f"Usuário '{nome}' adicionado com sucesso! ID: {user_id}"
            except sqlite3.IntegrityError:
                return f"Erro: O email '{email}' já está cadastrado."

    def get_usuario(self, usuario_id: Optional[int] = None, nome: Optional[str] = None) -> List[Dict]:
        with self.conn as conn:
            cursor = conn.cursor()

            if usuario_id is not None:
                cursor.execute('SELECT * FROM usuario WHERE id = ?', (usuario_id,))
            elif nome is not None:
                cursor.execute('SELECT * FROM usuario WHERE nome = ?', (nome,))
            else:
                cursor.execute('SELECT * FROM usuario')

            usuarios = cursor.fetchall()
            return [dict(u) for u in usuarios]

    def delete_usuario(self, usuario_id: int) -> str:
        with self.conn as conn:
            cursor = conn.cursor()
            cursor.execute('DELETE FROM usuario WHERE id = ?', (usuario_id,))
            conn.commit()

            if cursor.rowcount == 0:
                return f"Nenhum usuário com ID {usuario_id} encontrado."

            return f"Usuário ID {usuario_id} deletado com sucesso."

    def list_all(self) -> List[Dict]:
        return self.get_usuario()

    def __del__(self):
        
        self.conn.close()
