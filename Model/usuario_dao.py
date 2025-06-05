import sqlite3
from typing import List, Optional, Dict

class UsuarioDao:
    def __init__(self, dbpath: str):
        self.conn = sqlite3.connect(dbpath)
        self.conn.row_factory = sqlite3.Row
        self._create_table()

    def _create_table(self):
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

    def add_usuario(self, nome: str, idade: Optional[int], email: str) -> int:
        with self.conn as conn:
            cursor = conn.cursor()
            cursor.execute('''
                INSERT INTO usuario (nome, idade, email)
                VALUES (?, ?, ?)
            ''', (nome, idade, email))
            conn.commit()
            if cursor.lastrowid is None:
                raise ValueError("Erro ao inserir usuário. Verifique os dados fornecidos.")
            return cursor.lastrowid
            

    def update_usuario(self, usuario_id: int, nome: str, idade: Optional[int], email: str):
        with self.conn as conn:
            cursor = conn.cursor()
            cursor.execute('''
                UPDATE usuario
                SET nome = ?, idade = ?, email = ?
                WHERE id = ?
            ''', (nome, idade, email, usuario_id))
            conn.commit()

    def get_usuario(self, usuario_id: Optional[int] = None, nome: Optional[str] = None) -> Optional[Dict]:
        with self.conn as conn:
            cursor = conn.cursor()
            if usuario_id is not None:
                cursor.execute('SELECT * FROM usuario WHERE id = ?', (usuario_id,))
            elif nome is not None:
                cursor.execute('SELECT * FROM usuario WHERE nome = ?', (nome,))
            else:
                return None
            result = cursor.fetchone()
            return dict(result) if result else None

    def delete_usuario(self, usuario_id: int):
        with self.conn as conn:
            cursor = conn.cursor()
            cursor.execute('DELETE FROM usuario WHERE id = ?', (usuario_id,))
            conn.commit()

    def list_usuarios(self) -> List[Dict]:
        with self.conn as conn:
            cursor = conn.cursor()
            cursor.execute('SELECT * FROM usuario')
            usuarios = cursor.fetchall()
            return [dict(u) for u in usuarios]

    def __del__(self):
        
        self.conn.close()

