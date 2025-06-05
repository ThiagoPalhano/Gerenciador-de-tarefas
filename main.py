from Controller.menu_tarefas import menu_tarefas, fechar_tarefas

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
    while True:
        print("\n--- MENU TAREFAS ---")
        print("1. Adicionar Tarefa")
        print("2. Atualizar Tarefa")
        print("3. Listar Tarefas por Usuário")
        print("4. Deletar Tarefa")
        print("0. Voltar")

        escolha = input("Escolha uma opção: ")

        if escolha == '1':
            usuario_id = input("ID do Usuário: ")
            nome = input("Nome da Tarefa: ")
            descricao = input("Descrição: ")
            data_vencimento = input("Data de Vencimento (YYYY-MM-DD): ")
            prioridade = input("Prioridade (baixa, média, alta): ")
            status = input("Status (pendente, em andamento, concluída): ")
            dados = {
                "usuario_id": int(usuario_id),
                "nome": nome,
                "descricao": descricao,
                "data_vencimento": data_vencimento,
                "prioridade": prioridade,
                "status": status
            }
            print(menu_tarefas("adicionar", dados))

        elif escolha == '2':
            id_tarefa = input("ID da Tarefa: ")
            usuario_id = input("ID do Usuário: ")
            nome = input("Novo Nome da Tarefa: ")
            descricao = input("Nova Descrição: ")
            data_vencimento = input("Nova Data de Vencimento (YYYY-MM-DD): ")
            prioridade = input("Nova Prioridade (baixa, média, alta): ")
            status = input("Novo Status (pendente, em andamento, concluída): ")
            dados = {
                "id_tarefa": int(id_tarefa),
                "usuario_id": int(usuario_id),
                "nome": nome,
                "descricao": descricao,
                "data_vencimento": data_vencimento,
                "prioridade": prioridade,
                "status": status
            }
            print(menu_tarefas("atualizar", dados))

        elif escolha == '3':
            usuario_id = input("ID do Usuário: ")
            tarefas_brutas = menu_tarefas("listar_por_usuario", {"usuario_id": int(usuario_id)})

            if isinstance(tarefas_brutas, list) and tarefas_brutas:
                print("\n--- TAREFAS DO USUÁRIO ---")
                for t in tarefas_brutas:
                    t_formatada = formatar_tarefa(t)
                    print(
                        f"ID: {t_formatada['id']} | Nome: {t_formatada['nome']} | Descrição: {t_formatada['descricao']} | "
                        f"Vencimento: {t_formatada['data_vencimento']} | Prioridade: {t_formatada['prioridade']} | Status: {t_formatada['status']}"
                    )
            else:
                print("Nenhuma tarefa encontrada para este usuário.")

        elif escolha == '4':
            id_tarefa = input("ID da Tarefa: ")
            print(menu_tarefas("deletar", {"id_tarefa": int(id_tarefa)}))

        elif escolha == '0':
            break

        else:
            print("Opção inválida.")

def fechar():
    fechar_tarefas()

if __name__ == "__main__":
    gerenciar_tarefas()
    fechar()
