import sqlite3

class GerenciadorDAO :

    def __init__(self, dao: str):
        self.dao = dao
        self.conn = sqlite3.connect(self.dao)
        self.cur = self.conn.cursor()
        self.tarefas()

    def tarefas(self):
        query = '''
        CREATE TABLE IF NOT EXISTS tarefas (
           id INTEGER PRIMARY KEY AUTOINCREMENT,
           nome_tarefa TEXT NOT NULL,
           descricao TEXT NOT NULL,
           data_criacao DATETIME,
           data_vencimento DATETIME,
           prioridade TEXT NOT NULL,
           status_tarefa TEXT NOT NULL,
        )
        ''' 
        self.cur.execute(query)
        self.conn.commit()

    def fechar_conexao(self):
            self.cur.close()
            self.conn.close()  


dao = GerenciadorDAO("GerenciadorDAO.db")
dao.fechar_conexao()
