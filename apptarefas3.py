from datetime import datetime

def is_valid_priority(priority):
    return priority in ["alta", "média", "baixa"]

def is_valid_date(date):
    try:
        datetime.strptime(date, '%Y-%m-%d')
        return True
    except ValueError:
        return False

def main():
    tasks = []

    while True:
        print("\nEscolha uma opção:")
        print("1 - Cadastrar tarefa")
        print("2 - Listar tarefas")
        print("3 - Sair")

        choice = input("Digite o número da opção: ")

        if choice == "1":
            description = input("Digite a descrição da tarefa: ")
            due_date = input("Digite a data de vencimento (AAAA-MM-DD): ")
            priority = input("Digite a prioridade (alta, média ou baixa): ")

            if is_valid_priority(priority) and is_valid_date(due_date):
                tasks.append({"description": description, "due_date": due_date, "priority": priority})
                print("Tarefa cadastrada com sucesso!")
            else:
                print("Prioridade ou data inválida. Tarefa não cadastrada.")

        elif choice == "2":
            if tasks:
                print("\nTarefas:")
                for i, task in enumerate(tasks, 1):
                    print(f"{i} - Descrição: {task['description']}, Data de Vencimento: {task['due_date']}, Prioridade: {task['priority']}")
            else:
                print("Nenhuma tarefa cadastrada.")

        elif choice == "3":
            print("Saindo do aplicativo.")
            break

        else:
            print("Opção inválida. Por favor, escolha uma opção válida.")

if __name__ == "__main__":
    main()


