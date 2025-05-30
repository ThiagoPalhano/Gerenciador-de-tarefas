from typing import Optional, List
from gerenciador_dao import GerenciadorDao


class Tarefa:
    dao: Optional[GerenciadorDao] = None

    def __init__(self, id: Optional[int], usuario_id: int, tarefa_nome: str, descricao: str,
                 data_criacao: str, data_vencimento: str, prioridade: str, status: str):
        self.id = id
        self.usuario_id = usuario_id
        self.tarefa_nome = tarefa_nome
        self.descricao = descricao
        self.data_criacao = data_criacao
        self.data_vencimento = data_vencimento
        self.prioridade = prioridade
        self.status = status

    @classmethod
    def set_dao(cls, dao: GerenciadorDao):
        cls.dao = dao

    def save(self):

        if self.id is None:
            self.id = self.dao.create_tarefa(
                self.usuario_id,
                self.tarefa_nome,
                self.descricao,
                self.data_criacao,
                self.data_vencimento,
                self.prioridade,
                self.status
            )
        else:
            self.dao.update_tarefa(
                self.id,
                self.usuario_id,
                self.tarefa_nome,
                self.descricao,
                self.data_criacao,
                self.data_vencimento,
                self.prioridade,
                self.status
            )

    def delete(self):
        if self.id is not None:
            self.dao.delete_tarefa(self.id)
            self.id = None

    @classmethod
    def get(cls, tarefa_id: int) -> Optional["Tarefa"]:
        if cls.dao is None:
            raise ValueError("DAO não configurado. Use Tarefa.set_dao() para configurar.")

        data = cls.dao.get_tarefa(tarefa_id)
        if data:
            return cls(
                id=data["id"],
                usuario_id=data["usuario_id"],
                tarefa_nome=data["tarefa_nome"],
                descricao=data["descricao"],
                data_criacao=data["data_criacao"],
                data_vencimento=data["data_vencimento"],
                prioridade=data["prioridade"],
                status=data["status_tarefa"],
            )
        return None

    @classmethod
    def all(cls) -> List["Tarefa"]:
        if cls.dao is None:
            raise ValueError("DAO não configurado. Use Tarefa.set_dao() para configurar.")

        tarefas_data = cls.dao.list_tarefas()
        return [
            cls(
                id=data["id"],
                usuario_id=data["usuario_id"],
                tarefa_nome=data["tarefa_nome"],
                descricao=data["descricao"],
                data_criacao=data["data_criacao"],
                data_vencimento=data["data_vencimento"],
                prioridade=data["prioridade"],
                status=data["status_tarefa"],
            )
            for data in tarefas_data
        ]
