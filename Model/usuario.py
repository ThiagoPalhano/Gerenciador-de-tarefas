import sqlite3

class Usuarios :

    def __init__(self, usuario: str):
        self.usuario = usuario
        self.conn = sqlite3.Connection(self.usuario)
        self.cur = self.conn.cursor()
        self.usuarios()

    def usuarios (self):
        query = ('''
        CREATE TABLE IF NOT EXISTS usuario (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL,
        idade INTEGER,
        email TEXT UNIQUE
    )
''')
        self.cur.execute(query)
        self.conn.commit()

    def fechar_conexao(self):
            self.cur.close()
            self.conn.close()  


usuario = Usuarios("GerenciadorDAO.db")
usuario.fechar_conexao()
