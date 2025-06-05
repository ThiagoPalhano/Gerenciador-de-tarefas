
from typing import Optional, List
from Model.usuario_dao import UsuarioDao


class Usuario:
    dao: Optional[UsuarioDao] = None

    def __init__(self, id: Optional[int], nome: str, idade: int, email: str):
        self.id = id
        self.nome = nome
        self.idade = idade
        self.email = email


    @classmethod
    def set_dao(cls, dao: UsuarioDao):
        cls.dao = dao

    def save(self):
        if self.dao is None:
            raise ValueError("DAO não configurado. Use Usuario.set_dao().")

        if self.id is None:
            self.id = self.dao.add_usuario(
                self.nome,
                self.idade,
                self.email
            )
        else:
            self.dao.update_usuario(
                self.id,
                self.nome,
                self.idade,
                self.email
            )

    def delete(self):
        if self.dao is None:
            raise ValueError("DAO não configurado. Use Usuario.set_dao().")
        
        if self.id is not None:
            usuario_id = int(self.id)
            self.dao.delete_usuario(usuario_id)
            self.id = None

    @classmethod
    def get(cls, usuario_id: int) -> Optional["Usuario"]:
        if cls.dao is None:
            raise ValueError("DAO não configurado. Use Usuario.set_dao().")
        
        data = cls.dao.get_usuario(usuario_id)
        if data:
            return cls(
                id=data["id"],
                nome=data["nome"],
                idade=data["idade"],
                email=data["email"]
            )
        return None

    @classmethod
    def all(cls) -> List["Usuario"]:
        if cls.dao is None:
            raise ValueError("DAO não configurado. Use Usuario.set_dao().")

        usuarios_data = cls.dao.list_usuarios()
        return [
            cls(
                id=data["id"],
                nome=data["nome"],
                idade=data["idade"],
                email=data["email"]
            )
            for data in usuarios_data
        ]
