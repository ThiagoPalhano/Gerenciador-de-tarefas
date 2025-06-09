from Model.usuarios_dao import UsuarioDao

usuario_dao = UsuarioDao("gerenciador_de_tarefas.db")

def menu_usuarios(acao: str, dados: dict):
    try:
        if acao == "adicionar":
            nome = str(dados["nome"])
            idade = int(dados["idade"]) if dados.get("idade") else None
            email = str(dados["email"])
            usuario_id = usuario_dao.add_usuario(nome, idade, email)
            return f"Usuário criado com ID: {usuario_id}"

        elif acao == "atualizar":
            usuario_id = int(dados["id"])
            nome = str(dados["nome"])
            idade = int(dados["idade"]) if dados.get("idade") else None
            email = str(dados["email"])
            usuario_dao.update_usuario(usuario_id, nome, idade, email)
            return "Usuário atualizado com sucesso!"

        elif acao == "buscar":
            usuario_id = dados.get("id")
            nome = dados.get("nome")
            if usuario_id:
                usuario = usuario_dao.get_usuario(usuario_id=int(usuario_id))
            elif nome:
                usuario = usuario_dao.get_usuario(nome=str(nome))
            else:
                return "Informe id ou nome para buscar o usuário."
            return usuario if usuario else "Usuário não encontrado."

        elif acao == "listar":
            usuarios = usuario_dao.list_usuarios()
            return usuarios if usuarios else "Nenhum usuário encontrado."

        elif acao == "deletar":
            usuario_id = int(dados["id"])
            usuario_dao.delete_usuario(usuario_id)
            return "Usuário deletado com sucesso."

        else:
            return "Ação inválida."

    except KeyError as e:
        return f"Falta o dado: {e}"
    except Exception as e:
        return f"Erro: {e}"

def fechar_usuarios():
    usuario_dao.conn.close()

