from Model.gerenciador_tarefas import GerenciadorDao
from datetime import datetime

gerenciador = GerenciadorDao("GerenciadorDAO.db")

def menu_tarefas(acao: str, dados: dict):
    try:
        if acao == "adicionar":
            usuario_id = dados.get("usuario_id")
            nome = dados.get("nome")
            descricao = dados.get("descricao")
            data_criacao = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            data_venc = dados.get("data_venc")
            prioridade = dados.get("prioridade")
            status = dados.get("status")

            tarefa_id = gerenciador.create_tarefa(
                usuario_id, nome, descricao, data_criacao, data_venc, prioridade, status
            )
            return f"Tarefa criada com ID: {tarefa_id}"

        elif acao == "atualizar":
            id_tarefa = dados.get("id_tarefa")
            usuario_id = dados.get("usuario_id")
            nome = dados.get("nome")
            descricao = dados.get("descricao")
            data_criacao = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            data_venc = dados.get("data_venc")
            prioridade = dados.get("prioridade")
            status = dados.get("status")

            gerenciador.update_tarefa(
                id_tarefa, usuario_id, nome, descricao, data_criacao, data_venc, prioridade, status
            )
            return "Tarefa atualizada com sucesso!"

        elif acao == "listar_por_usuario":
            usuario_id = dados.get("usuario_id")
            tarefas = gerenciador.list_tarefas_por_usuario(usuario_id)
            if tarefas:
                return [dict(t) for t in tarefas]
            else:
                return "Nenhuma tarefa encontrada."

        elif acao == "deletar":
            id_tarefa = dados.get("id_tarefa")
            gerenciador.delete_tarefa(id_tarefa)
            return "Tarefa deletada com sucesso."

        else:
            return "Ação inválida."
    except Exception as e:
        return f"Erro: {e}"

def fechar_tarefas():
    gerenciador.conn.close()
