from Controller.menu_usuarios import menu_usuarios, fechar_usuarios
from Controller.menu_tarefas import menu_tarefas, fechar_tarefas


def gerenciar_usuarios():
    while True:
        print("\n--- MENU USUÁRIOS ---")
        print("1. Adicionar Usuário")
        print("2. Atualizar Usuário")
        print("3. Buscar Usuário")
        print("4. Listar Usuários")
        print("5. Deletar Usuário")
        print("0. Voltar")

        escolha = input("Escolha uma opção: ").strip()

        if escolha == '1':
            nome = input("Nome: ").strip()
            idade = input("Idade (ou deixe vazio): ").strip()
            email = input("Email: ").strip()
            dados = {"nome": nome, "idade": int(idade) if idade else None, "email": email}
            print(menu_usuarios("adicionar", dados))

        elif escolha == '2':
            id_usuario = input("ID do usuário: ").strip()
            nome = input("Novo Nome: ").strip()
            idade = input("Nova Idade (ou deixe vazio): ").strip()
            email = input("Novo Email: ").strip()
            dados = {"id": int(id_usuario), "nome": nome, "idade": int(idade) if idade else None, "email": email}
            print(menu_usuarios("atualizar", dados))

        elif escolha == '3':
            buscar = input("Buscar por (1) ID ou (2) Nome? ").strip()
            if buscar == '1':
                id_usuario = input("ID: ").strip()
                print(menu_usuarios("buscar", {"id": int(id_usuario)}))
            elif buscar == '2':
                nome = input("Nome: ").strip()
                print(menu_usuarios("buscar", {"nome": nome}))
            else:
                print("Opção inválida.")

        elif escolha == '4':
            resultado = menu_usuarios("listar", {})
            if isinstance(resultado, list) and resultado:
                print("\n--- LISTA DE USUÁRIOS ---")
                for u in resultado:
                    idade = u["idade"] if u["idade"] is not None else "Não informada"
                    print(f"ID: {u['id']} | Nome: {u['nome']} | Idade: {idade} | Email: {u['email']}")
            elif isinstance(resultado, list) and not resultado:
                print("Nenhum usuário encontrado.")
            else:
                print(resultado)

        elif escolha == '5':
            id_usuario = input("ID do usuário: ").strip()
            print(menu_usuarios("deletar", {"id": int(id_usuario)}))

        elif escolha == '0':
            break
        else:
            print("Opção inválida.")


def formatar_tarefa(tarefa: dict) -> dict:
    return {
        "id": tarefa["id"],
        "usuario_id": tarefa["usuario_ID"],
        "nome": tarefa["tarefa_nome"],
        "descricao": tarefa["descricao"],
        "data_criacao": tarefa["data_criacao"],
        "data_vencimento": tarefa["data_vencimento"],
        "prioridade": tarefa["prioridade"],
        "status": tarefa["status_tarefa"],
    }


def gerenciar_tarefas():
    print("\n--- LOGIN DE USUÁRIO ---")
    usuario_id = input("Informe seu ID de usuário: ").strip()

    usuario = menu_usuarios("buscar", {"id": int(usuario_id)})
    if not isinstance(usuario, dict):
        print("Usuário não encontrado. Retornando ao menu principal.")
        return
    print(f"Bem-vindo, {usuario['nome']}!")

    while True:
        print("\n--- MENU TAREFAS ---")
        print("1. Adicionar Tarefa")
        print("2. Atualizar Tarefa")
        print("3. Listar Minhas Tarefas")
        print("4. Deletar Tarefa")
        print("0. Voltar")

        escolha = input("Escolha uma opção: ").strip()

        if escolha == '1':
            nome = input("Nome da Tarefa: ").strip()
            descricao = input("Descrição: ").strip()
            data_vencimento = input("Data de Vencimento (YYYY-MM-DD): ").strip()
            prioridade = input("Prioridade (baixa, média, alta): ").strip()
            status = input("Status (pendente, em andamento, concluída): ").strip()

            dados = {
                "usuario_id": int(usuario_id),
                "nome": nome,
                "descricao": descricao,
                "data_vencimento": data_vencimento,
                "prioridade": prioridade,
                "status": status,
            }
            print(menu_tarefas("adicionar", dados))

        elif escolha == '2':
            id_tarefa = input("ID da Tarefa: ").strip()
            nome = input("Novo Nome da Tarefa: ").strip()
            descricao = input("Nova Descrição: ").strip()
            data_vencimento = input("Nova Data de Vencimento (YYYY-MM-DD): ").strip()
            prioridade = input("Nova Prioridade (baixa, média, alta): ").strip()
            status = input("Novo Status (pendente, em andamento, concluída): ").strip()

            dados = {
                "id_tarefa": int(id_tarefa),
                "usuario_id": int(usuario_id),
                "nome": nome,
                "descricao": descricao,
                "data_vencimento": data_vencimento,
                "prioridade": prioridade,
                "status": status,
            }
            print(menu_tarefas("atualizar", dados))

        elif escolha == '3':
            tarefas_brutas = menu_tarefas("listar_por_usuario", {"usuario_id": int(usuario_id)})

            if isinstance(tarefas_brutas, list) and tarefas_brutas:
                print("\n--- SUAS TAREFAS ---")
                for t in tarefas_brutas:
                    t_formatada = formatar_tarefa(t)
                    print(
                        f"ID: {t_formatada['id']} | Nome: {t_formatada['nome']} | Descrição: {t_formatada['descricao']} | "
                        f"Vencimento: {t_formatada['data_vencimento']} | Prioridade: {t_formatada['prioridade']} | Status: {t_formatada['status']}"
                    )
            else:
                print("Você não possui tarefas registradas.")

        elif escolha == '4':
            id_tarefa = input("ID da Tarefa a deletar: ").strip()
            resultado = menu_tarefas("deletar_por_usuario", {"id_tarefa": int(id_tarefa), "usuario_id": int(usuario_id)})
            print(resultado)

        elif escolha == '0':
            break
        else:
            print("Opção inválida.")


def main():
    while True:
        print("\n===== MENU PRINCIPAL =====")
        print("1. Usuários")
        print("2. Tarefas")
        print("0. Sair")

        escolha = input("Escolha uma opção: ").strip()

        if escolha == '1':
            gerenciar_usuarios()
        elif escolha == '2':
            gerenciar_tarefas()
        elif escolha == '0':
            print("Saindo...")
            fechar_usuarios()
            fechar_tarefas()
            break
        else:
            print("Opção inválida. Tente novamente.")


if __name__ == "__main__":
    main()
