

from Model.usuarios import Usuario

def menu_usuarios(acao: str, dados: dict):
    try:
        if acao == "adicionar":
            nome = str(dados["nome"])
            idade = int(dados["idade"]) if dados.get("idade") else None
            email = str(dados["email"])
            usuario = Usuario(None, nome, idade, email)
            usuario.save()
            return f"Usuário criado com ID: {usuario.id}"

        elif acao == "atualizar":
            usuario_id = int(dados["id"])
            nome = str(dados["nome"])
            idade = int(dados["idade"]) if dados.get("idade") else None
            email = str(dados["email"])
            usuario = Usuario.get(usuario_id)
            if not usuario:
                return "Usuário não encontrado."
            usuario.nome = nome
            usuario.idade = idade
            usuario.email = email
            usuario.save()
            return "Usuário atualizado com sucesso!"

        elif acao == "buscar":
            usuario_id = dados.get("id")
            if usuario_id:
                usuario = Usuario.get(int(usuario_id))
            else:
                return "Informe id para buscar o usuário."
            return usuario.to_dict() if usuario else "Usuário não encontrado."

        elif acao == "listar":
            usuarios = Usuario.all()
            return [u.to_dict() for u in usuarios] if usuarios else "Nenhum usuário encontrado."

        elif acao == "deletar":
            usuario_id = int(dados["id"])
            usuario = Usuario.get(usuario_id)
            if not usuario:
                return "Usuário não encontrado."
            usuario.delete()
            return "Usuário deletado com sucesso."

        else:
            return "Ação inválida."

    except KeyError as e:
        return f"Falta o dado: {e}"
    except Exception as e:
        return f"Erro: {e}"

def fechar_usuarios():

        pass

