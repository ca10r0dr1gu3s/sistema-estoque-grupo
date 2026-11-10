tarefas = []


# ==============================
# VALIDAÇÃO DOS CADASTROS (Lauro)
# ==============================

def validar_texto(mensagem):
    while True:
        texto = input(mensagem).strip()
        if texto != "":
            return texto
        else:
            print("Erro: o campo não pode ficar vazio!")


def validar_prioridade():
    while True:
        prioridade = input("Prioridade (Baixa, Média ou Alta): ").strip()
        if prioridade in ["Baixa", "Média", "Alta"]:
            return prioridade
        else:
            print("Erro: informe exatamente Baixa, Média ou Alta.")


def validar_id():
    try:
        id_tarefa = int(input("Digite o ID da tarefa: "))
        if id_tarefa > 0:
            return id_tarefa
        else:
            print("Erro: o ID deve ser maior que zero.")
            return None
    except ValueError:
        print("Erro: informe um ID numérico válido.")
        return None


# ==============================
# BUSCA E GESTÃO (Lauro & Caio)
# ==============================

def buscar_tarefa(id_tarefa):
    for tarefa in tarefas:
        if tarefa["id"] == id_tarefa:
            return tarefa
    return None


def cadastrar_tarefa():
    print("\n===== CADASTRAR TAREFA =====")
    titulo = validar_texto("Título: ")
    descricao = validar_texto("Descrição: ")
    prioridade = validar_prioridade()

    if len(tarefas) == 0:
        novo_id = 1
    else:
        maior_id = max(t["id"] for t in tarefas)
        novo_id = maior_id + 1

    nova_tarefa = {
        "id": novo_id,
        "titulo": titulo,
        "descricao": descricao,
        "prioridade": prioridade,
        "status": "Pendente"
    }

    tarefas.append(nova_tarefa)
    print("\nTarefa cadastrada com sucesso!")
    print("ID da tarefa:", novo_id)


def editar_tarefa():
    print("\n===== EDITAR TAREFA =====")
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

    print("\nDeixe o campo vazio para manter o valor atual.")
    print("Título atual:", tarefa["titulo"])
    novo_titulo = input("Novo título: ").strip()
    if novo_titulo != "":
        tarefa["titulo"] = novo_titulo

    print("Descrição atual:", tarefa["descricao"])
    nova_descricao = input("Nova descrição: ").strip()
    if nova_descricao != "":
        tarefa["descricao"] = nova_descricao

    print("Prioridade atual:", tarefa["prioridade"])
    while True:
        nova_prioridade = input("Nova prioridade (Baixa, Média ou Alta): ").strip()
        if nova_prioridade == "":
            break
        if nova_prioridade in ["Baixa", "Média", "Alta"]:
            tarefa["prioridade"] = nova_prioridade
            break
        else:
            print("Erro: prioridade inválida.")

    print("\nTarefa atualizada com sucesso!")


def excluir_tarefa():
    print("\n===== EXCLUIR TAREFA =====")
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

    print("\nTarefa selecionada:", tarefa["titulo"])
    confirmacao = input("Deseja realmente excluir esta tarefa? (S/N): ").strip().upper()

    if confirmacao == "S":
        tarefas.remove(tarefa)
        print("Tarefa excluída com sucesso!")
    else:
        print("Exclusão cancelada.")


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
# LISTAGEM E RELATÓRIOS (Luan)
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


# ==============================
# MENU INTERATIVO PRINCIPAL (Caio)
# ==============================

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


def main():
    while True:
        exibir_menu()
        opcao = input("Escolha uma opção: ").strip()

        if opcao == "1":
            cadastrar_tarefa()
        elif opcao == "2":
            listar_tarefas()
        elif opcao == "3":
            concluir_tarefa()
        elif opcao == "4":
            editar_tarefa()
        elif opcao == "5":
            excluir_tarefa()
        elif opcao == "6":
            exibir_relatorio()
        elif opcao == "0":
            print("\nEncerrando o programa. Até logo!")
            break
        else:
            print("Opção inválida! Tente novamente.")


if __name__ == "__main__":
    main()
