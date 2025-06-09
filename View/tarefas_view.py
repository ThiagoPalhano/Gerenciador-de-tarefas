from Controller.menu_tarefas import menu_tarefas
from Controller.menu_usuarios import menu_usuarios

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
