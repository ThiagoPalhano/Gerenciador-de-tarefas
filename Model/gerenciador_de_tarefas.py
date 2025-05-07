import sqlite3
from datetime import datetime

class GerenciadorTarefas:
    def __init__(self, banco: str):
    
        self.banco = banco
        self.conn = sqlite3.connect(self.banco)
        self.criar_tabelas()

    def renomear_coluna(self, tabela: str, coluna_antiga: str, coluna_nova: str):
    
        with self.conn as conn:
            cursor = conn.cursor()
            try:
                cursor.execute(f"ALTER TABLE {tabela} RENAME COLUMN {coluna_antiga} TO {coluna_nova};")
                conn.commit()
                return f"Coluna '{coluna_antiga}' renomeada para '{coluna_nova}' na tabela '{tabela}'."
            except sqlite3.OperationalError:
                return f"Erro: Não foi possível renomear a coluna '{coluna_antiga}'. Verifique se a tabela ou coluna existem."

    def criar_tabelas(self):
    
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

            cursor.execute('''
                CREATE TABLE IF NOT EXISTS tarefas (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    usuario_id INTEGER,
                    tarefa_nome TEXT NOT NULL,
                    descricao TEXT NOT NULL,
                    data_criacao DATETIME NOT NULL,
                    data_vencimento DATETIME NOT NULL,
                    prioridade TEXT NOT NULL,
                    status_tarefa TEXT NOT NULL,
                    FOREIGN KEY (usuario_id) REFERENCES usuario(id) ON DELETE CASCADE
                )
            ''')
            conn.commit()

    def adicionar_usuario(self, nome: str, idade: int, email: str) -> str:
    
        with self.conn as conn:
            cursor = conn.cursor()
            try:
                cursor.execute('''
                    INSERT INTO usuario (nome, idade, email)
                    VALUES (?, ?, ?)
                ''', (nome, idade, email))
                conn.commit()
                return f"Usuário '{nome}' adicionado com sucesso!"
            except sqlite3.IntegrityError:
                return f"Erro: O email '{email}' já está cadastrado."
            
    def consultar_usuario(self, usuario_id: int = None, nome: str = None) -> list:

        with self.conn as conn:
         cursor = conn.cursor()

        if usuario_id:
            cursor.execute('SELECT id, nome, idade, email FROM usuario WHERE id = ?', (usuario_id,))
        elif nome:
            cursor.execute('SELECT id, nome, idade, email FROM usuario WHERE nome = ?', (nome,))
        else:
            return "Erro: É necessário informar o ID ou o nome do usuário."

        usuario = cursor.fetchall()
        return usuario if usuario else "Nenhum usuário encontrado." 
    

    def adicionar_tarefa(self, usuario_id: int, tarefa_nome: str, descricao: str, data_vencimento: str, prioridade: str, status="Pendente") -> str:
    
        data_criacao = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        with self.conn as conn:
            cursor = conn.cursor()
            cursor.execute('SELECT id FROM usuario WHERE id = ?', (usuario_id,))
            if cursor.fetchone():
                cursor.execute('''
                        INSERT INTO tarefas (usuario_id, tarefa_nome, descricao, data_criacao, data_vencimento, prioridade, status_tarefa)
                        VALUES (?, ?, ?, ?, ?, ?, ?)
                ''', (usuario_id, tarefa_nome, descricao, data_criacao, data_vencimento, prioridade, status))  

                conn.commit()
                return f"Tarefa '{tarefa_nome}' adicionada para o usuário ID {usuario_id}!"
            else:
                return f"Erro: Nenhum usuário encontrado com ID {usuario_id}."
            
    def deletar_tarefa(self, id: int = None, tarefa_nome: str = None) -> str:
        with self.conn as conn:
            cursor = conn.cursor()

        if id:
            cursor.execute('SELECT id FROM tarefas WHERE id = ?', (id,))
        elif tarefa_nome:
            cursor.execute('SELECT id FROM tarefas WHERE tarefa_nome = ?', (tarefa_nome,))
        else:
            return "Erro: Você deve fornecer um ID ou um nome de tarefa para deletar."

        if cursor.fetchone():
            if id:
                cursor.execute('DELETE FROM tarefas WHERE id = ?', (id,))
            else:
                cursor.execute('DELETE FROM tarefas WHERE tarefa_nome = ?', (tarefa_nome,))
            conn.commit()
            return f"A tarefa foi deletada com sucesso!"
        else:
            return f"Erro: Nenhuma tarefa encontrada com os critérios informados."

    def consultar_tarefas(self, usuario_id: int) -> list:
    
        with self.conn as conn:
            cursor = conn.cursor()
            cursor.execute('SELECT id, tarefa_nome, descricao, prioridade, status_tarefa FROM tarefas WHERE usuario_id = ?', (usuario_id,))
            tarefas = cursor.fetchall()

        return tarefas if tarefas else []

    def fechar_conexao(self):

        self.conn.close()

# Instanciando o gerenciador
gerenciador = GerenciadorTarefas("GerenciadorDAO.db")

# Renomeando colunas do banco de dados

#print(gerenciador.renomear_coluna("tarefas", "tarefa", "tarefa_nome"))

# Adicionando usuários
#print(gerenciador.adicionar_usuario("Thiago", 30, "thiago@email.com"))
#print(gerenciador.adicionar_usuario("Camilo", 28, "camilo@email.com"))"""

# Adicionando tarefas
#print(gerenciador.adicionar_tarefa(2, "Agendar exame cardio", "Ligar para o 0800 da prefeitura", "2025-04-30", "Alta"))
#print(gerenciador.adicionar_tarefa(1, "Reunião com Paulo", "Discutir progresso do projeto", "2025-04-29", "Média"))

# Consultando tarefas
"""tarefas_encontradas = gerenciador.consultar_tarefas(1)

if tarefas_encontradas:
    print("\nTarefas de {usuario_nome}:")
    print("-" * 50)
    for tarefa in tarefas_encontradas:
        print(f"ID: {tarefa[0]} | Tarefa: {tarefa[1]} | Descrição: {tarefa[2]} | Prioridade: {tarefa[3]} | Status: {tarefa[4]}")
else:
print("Nenhuma tarefa encontrada.")"""

# Deletando tarefas
"""resultado = gerenciador.deletar_tarefa(tarefa_nome="Reunião com Paulo")  

if "sucesso" in resultado.lower():
    print(f"Tarefa removida com sucesso! {resultado}")
elif "erro" in resultado.lower():
    print(f"Falha ao remover tarefa: {resultado}")
else:
    print(f"Informação: {resultado}")"""

    
    
gerenciador.fechar_conexao()
