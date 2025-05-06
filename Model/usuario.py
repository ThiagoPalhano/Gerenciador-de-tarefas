import sqlite3

class Usuarios:
    def __init__(self, banco: str):
        self.banco = banco
        self.conn = sqlite3.connect(self.banco)
        self.cur = self.conn.cursor()
        self.criar_tabela()

    def criar_tabela(self):
        query = '''
        CREATE TABLE IF NOT EXISTS usuario (
            id INTEGER PRIMARY KEY,
            nome TEXT NOT NULL,
            idade INTEGER,
            email TEXT UNIQUE
        )
        '''
        self.cur.execute(query)
        self.conn.commit()

    def adicionar_usuario(self, nome: str, idade: int, email: str):
        with sqlite3.connect(self.banco) as conn:
            cursor = conn.cursor()
            try:
                cursor.execute('''
                    INSERT INTO usuario (nome, idade, email)
                    VALUES (?, ?, ?)
                ''', (nome, idade, email))
                conn.commit()
                print(f"Usuário '{nome}' adicionado com sucesso!")
            except sqlite3.IntegrityError:
                print(f"Erro: O email '{email}' já está cadastrado.")

    def consultar_usuarios(self):
        with sqlite3.connect(self.banco) as conn:
            cursor = conn.cursor()
            cursor.execute('SELECT * FROM usuario')
            usuarios = cursor.fetchall()

            if usuarios:
                print("\nLista de Usuários:")
                print("-" * 50)
                for usuario in usuarios:
                    print(f"ID: {usuario[0]} | Nome: {usuario[1]} | Idade: {usuario[2]} | Email: {usuario[3]}")
            else:
                print("Nenhum usuário encontrado.")

    def fechar_conexao(self):
        self.cur.close()
        self.conn.close()

usuario_db = Usuarios("GerenciadorDOA.db")
usuario_db.adicionar_usuario("Thiago de Lima Palhano", 34, "thiagolimapalhano@email.com")


usuario_db.consultar_usuarios()

usuario_db.fechar_conexao()