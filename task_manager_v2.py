tarefas = []

while True:
    print("\n=== GERENCIADOR DE TAREFAS ===")
    print("1 - Adicionar tarefa")
    print("2 - Ver tarefas")
    print("3 - Remover tarefa")
    print("4 - Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        tarefa = input("Digite a nova tarefa: ")
        tarefas.append(tarefa)
        print("Tarefa adicionada!")

    elif opcao == "2":
        if len(tarefas) == 0:
            print("Nenhuma tarefa.")
        else:
            print("\nLista de tarefas:")
            for i, t in enumerate(tarefas):
                print(i + 1, "-", t)

    elif opcao == "3":
        numero = int(input("Número da tarefa para remover: "))
        if numero <= len(tarefas):
            tarefas.pop(numero - 1)
            print("Tarefa removida!")
        else:
            print("Tarefa não encontrada.")

    elif opcao == "4":
        print("Encerrando programa...")
        break

    else:
        print("Opção inválida.")
