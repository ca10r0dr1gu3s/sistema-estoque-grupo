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


# ==============================
# LISTAGEM DE TAREFAS (Luan - naskjz)
# ==============================

def listar_tarefas():
    print("\n" + "="*56)
    print("                LISTA DE TAREFAS")
    print("="*56)
    if len(tarefas) == 0:
        print("Nenhuma tarefa cadastrada no momento.")
        print("="*56)
        return

    print(f"{'ID':<4} | {'Título':<22} | {'Prioridade':<10} | {'Status':<10}")
    print("-" * 56)
    for t in tarefas:
        titulo = t.get("titulo", "Sem título")
        if len(titulo) > 20:
            titulo = titulo[:19] + "…"
        prioridade = t.get("prioridade", "Média")
        status = t.get("status", "Pendente")
        print(f"{t['id']:<4} | {titulo:<22} | {prioridade:<10} | {status:<10}")
    print("="*56)


# ==============================
# RELATÓRIOS E ESTATÍSTICAS (Luan - naskjz)
# ==============================

def exibir_relatorio():
    print("\n" + "="*40)
    print("       RELATÓRIO DE PRODUTIVIDADE")
    print("="*40)
    total = len(tarefas)
    if total == 0:
        print("Sem dados para gerar estatísticas.")
        print("="*40)
        return

    concluidas = sum(1 for t in tarefas if t.get("status") == "Concluída")
    pendentes = total - concluidas
    alta = sum(1 for t in tarefas if t.get("prioridade") == "Alta")
    media = sum(1 for t in tarefas if t.get("prioridade") == "Média")
    baixa = sum(1 for t in tarefas if t.get("prioridade") == "Baixa")

    porcentagem_concluida = (concluidas / total) * 100
    porcentagem_pendente = (pendentes / total) * 100

    print(f"Total de tarefas cadastradas: {total}")
    print(f"Tarefas Concluídas: {concluidas} ({porcentagem_concluida:.1f}%)")
    print(f"Tarefas Pendentes:  {pendentes} ({porcentagem_pendente:.1f}%)")
    print("-" * 40)
    print("Distribuição por Prioridade:")
    print(f"  • Alta:  {alta}")
    print(f"  • Média: {media}")
    print(f"  • Baixa: {baixa}")
    print("="*40)


def main():
    while True:
        exibir_menu()
        opcao = input("Escolha uma opção: ").strip()
        if opcao == "1":
            print("[Aviso] Funcionalidade em desenvolvimento...")
        elif opcao == "2":
            listar_tarefas()
        elif opcao == "3":
            concluir_tarefa()
        elif opcao in ("4", "5"):
            print("[Aviso] Funcionalidade em desenvolvimento...")
        elif opcao == "6":
            exibir_relatorio()
        elif opcao == "0":
            print("Encerrando o programa. Até logo!")
            break
        else:
            print("Opção inválida! Tente novamente.")


if __name__ == "__main__":
    main()
