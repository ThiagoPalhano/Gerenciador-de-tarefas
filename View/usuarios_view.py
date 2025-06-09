
from Controller.menu_usuarios import menu_usuarios

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
