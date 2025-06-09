

from typing import Optional, List
from Model.usuarios_dao import UsuarioDao


class Usuario:
    def __init__(self, id: Optional[int], nome: str, idade: int, email: str, dao: Optional[UsuarioDao] = None):
        self.id = id
        self.nome = nome
        self.idade = idade
        self.email = email
        self.dao = dao or UsuarioDao("gerenciador_de_tarefas.db")

    def save(self):


        if self.id is None:
            self.id = self.dao.add_usuario(self.nome, self.idade, self.email)
        else:
            self.dao.update_usuario(self.id, self.nome, self.idade, self.email)

    def delete(self):
        

        if self.id is not None:
            self.dao.delete_usuario(self.id)
            self.id = None

    @classmethod
    def get(cls, usuario_id: int, dao: Optional[UsuarioDao] = None) -> Optional["Usuario"]:
        dao = dao or UsuarioDao("gerenciador_de_tarefas.db")
        data = dao.get_usuario(usuario_id)
        if data:
            return cls(
                id=data["id"],
                nome=data["nome"],
                idade=data["idade"],
                email=data["email"],
                dao=dao
            )
        return None

    @classmethod
    def all(cls, dao: Optional[UsuarioDao] = None) -> List["Usuario"]:
        dao = dao or UsuarioDao("gerenciador_de_tarefas.db")
        usuarios_data = dao.list_usuarios()
        return [
            cls(
                id=data["id"],
                nome=data["nome"],
                idade=data["idade"],
                email=data["email"],
                dao=dao
            )
            for data in usuarios_data
        ]
