from Model.tarefas import Tarefa
from datetime import datetime



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

            tarefa_id = Tarefa(
                usuario_id,
                nome,
                descricao,
                data_criacao,
                data_vencimento,
                prioridade,
                status
            )
            tarefa_id.save()
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

            tarefa_update = Tarefa(
                usuario_id,
                nome,
                descricao,
                data_criacao,
                data_vencimento,
                prioridade,
                status,
                id_tarefa
            )
            tarefa_update.save()
            return "Tarefa atualizada com sucesso!"

        elif acao == "listar_por_usuario":
            usuario_id = int(dados["usuario_id"])
            tarefa_list = Tarefa.all(None)
            if tarefa_list:
                return [t.to_dict() for t in tarefa_list]
            else:
                return "Nenhuma tarefa encontrada."

        elif acao == "deletar":
            id_tarefa = int(dados["id_tarefa"])
            tarefa = Tarefa.get(id_tarefa)
            if not tarefa:
                return "Tarefa não encontrada."
            if tarefa.usuario_id != int(dados["usuario_id"]):
                return "Você não tem permissão para deletar esta tarefa."
            tarefa.delete()
            return "Tarefa deletada com sucesso."
        
        else:
            return "Ação inválida."

    except KeyError as e:
        return f"Falta o dado: {e}"
    except Exception as e:
        return f"Erro: {e}"


