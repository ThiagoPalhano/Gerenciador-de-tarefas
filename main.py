

from View.usuarios_view import gerenciar_usuarios
from View.tarefas_view import gerenciar_tarefas         

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

            break
        else:
            print("Opção inválida. Tente novamente.")


if __name__ == "__main__":
    main()
