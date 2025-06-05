from Model.gerenciador_tarefas import GerenciadorDao
from datetime import datetime

gerenciador = GerenciadorDao("gerenciador_de_tarefas.db")

def menu_tarefas(acao: str, dados: dict):
    try:
        if acao == "adicionar":
        
            data_criacao = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            usuario_id = int(dados["usuario_id"])
            nome = str(dados["nome"])
            descricao = str(dados["descricao"])
            data_vencimento = str(dados["data_vencimento"])
            prioridade = str(dados["prioridade"])
            status = str(dados["status"])

            tarefa_id = gerenciador.create_tarefa(
                usuario_id,
                nome,
                descricao,
                data_criacao,
                data_vencimento,
                prioridade,
                status
            )
            return f"Tarefa criada com ID: {tarefa_id}"

        elif acao == "atualizar":

            data_criacao = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            id_tarefa = int(dados["id_tarefa"])
            usuario_id = int(dados["usuario_id"])
            nome = str(dados["nome"])
            descricao = str(dados["descricao"])
            data_vencimento = str(dados["data_vencimento"])
            prioridade = str(dados["prioridade"])
            status = str(dados["status"])

            gerenciador.update_tarefa(
                id_tarefa,
                nome,
                descricao,
                data_vencimento,
                prioridade,
                status
            )
            return "Tarefa atualizada com sucesso!"

        elif acao == "listar_por_usuario":
            usuario_id = int(dados["usuario_id"])
            tarefas = gerenciador.list_tarefas_por_usuario(usuario_id)
            if tarefas:
                return [dict(t) for t in tarefas]
            else:
                return "Nenhuma tarefa encontrada."

        elif acao == "deletar":
            id_tarefa = int(dados["id_tarefa"])
            gerenciador.delete_tarefa(id_tarefa)
            return "Tarefa deletada com sucesso."

        else:
            return "Ação inválida."

    except KeyError as e:
        return f"Falta o dado: {e}"
    except Exception as e:
        return f"Erro: {e}"

def fechar_tarefas():
    gerenciador.conn.close()
