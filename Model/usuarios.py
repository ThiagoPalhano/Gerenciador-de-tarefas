from typing import Optional, List
from gerenciador_dao import GerenciadorDao

class Usuario:
    dao: Optional[GerenciadorDao] = None

    def __init__(self, id: Optional[int], nome: str, email: str, senha: str):
        self.id = id
        self.nome = nome
        self.email = email
        self.senha = senha

    @classmethod
    def set_dao(cls, dao: GerenciadorDao):
        cls.dao = dao

    def save(self):
        if self.dao is None:
            raise ValueError("DAO não configurado. Use Usuario.set_dao() para configurar.")
        
        if self.id is None:
            self.id = self.dao.create_usuario(
                self.nome,
                self.email,
                self.senha
            )
        else:
            self.dao.update_usuario(
                self.id,
                self.nome,
                self.email,
                self.senha
            )

    def delete(self):
        if self.dao is None:
            raise ValueError("DAO não configurado. Use Usuario.set_dao() para configurar.")
        
        if self.id is not None:
            self.dao.delete_usuario(self.id)
            self.id = None

    @classmethod
    def get(cls, usuario_id: int) -> Optional["Usuario"]:
        if cls.dao is None:
            raise ValueError("DAO não configurado. Use Usuario.set_dao() para configurar.")
        
        data = cls.dao.get_usuario(usuario_id)
        if data:
            return cls(
                id=data["id"],
                nome=data["nome"],
                email=data["email"],
                senha=data["senha"]
            )
        return None

    @classmethod
    def all(cls) -> List["Usuario"]:
        if cls.dao is None:
            raise ValueError("DAO não configurado. Use Usuario.set_dao() para configurar.")

        usuarios_data = cls.dao.list_usuarios()
        return [
            cls(
                id=data["id"],
                nome=data["nome"],
                email=data["email"],
                senha=data["senha"]
            )
            for data in usuarios_data
        ]
