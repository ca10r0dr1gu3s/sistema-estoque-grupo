tarefas = []


def exibir_menu():
    print("\n" + "="*35)
    print("      GERENCIADOR DE TAREFAS")
    print("="*35)
    print("1 - Cadastrar tarefa")
    print("2 - Listar tarefas")
    print("3 - Concluir tarefa")
    print("4 - Editar tarefa")
    print("5 - Excluir tarefa")
    print("6 - Relatório geral")
    print("0 - Sair")
    print("="*35)


def validar_id():
    try:
        return int(input("ID da tarefa: ").strip())
    except ValueError:
        print("ID inválido!")
        return None


def buscar_tarefa(id_tarefa):
    return next((tarefa for tarefa in tarefas if tarefa["id"] == id_tarefa), None)


def concluir_tarefa():
    print("\n===== CONCLUIR TAREFA =====")
    if len(tarefas) == 0:
        print("Não existem tarefas cadastradas.")
        return
    id_tarefa = validar_id()
    if id_tarefa is None:
        return
    tarefa = buscar_tarefa(id_tarefa)
    if tarefa is None:
        print("Erro: tarefa não encontrada.")
        return
    tarefa["status"] = "Concluída"
    print(f"\nSucesso: Tarefa #{tarefa['id']} marcada como CONCLUÍDA!")


def main():
    global tarefas
    dados = []
    tarefas = dados
    while True:
        exibir_menu()
        opcao = input("Escolha uma opção: ").strip()
        if opcao == "1":
            print("[Aviso] Funcionalidade em desenvolvimento...")
        elif opcao == "2":
            print("[Aviso] Funcionalidade em desenvolvimento...")
        elif opcao == "3":
            concluir_tarefa()
        elif opcao in ("4", "5", "6"):
            print("[Aviso] Funcionalidade em desenvolvimento...")
        elif opcao == "0":
            print("Encerrando o programa. Até logo!")
            break
        else:
            print("Opção inválida! Tente novamente.")
if __name__ == "__main__":
    main()