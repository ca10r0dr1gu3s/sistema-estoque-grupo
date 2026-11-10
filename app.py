tarefas = []


# ==============================
# VALIDAÇÃO DOS CADASTROS
# ==============================

def validar_texto(mensagem):
    while True:
        texto = input(mensagem)

        if texto != "":
            return texto
        else:
            print("Erro: o campo não pode ficar vazio!")


def validar_prioridade():
    while True:
        prioridade = input(
            "Prioridade (Baixa, Média ou Alta): "
        )

        if prioridade == "Baixa" or prioridade == "Média" or prioridade == "Alta":
            return prioridade
        else:
            print("Erro: informe Baixa, Média ou Alta.")


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
# BUSCAR TAREFA
# ==============================

def buscar_tarefa(id_tarefa):
    for tarefa in tarefas:
        if tarefa["id"] == id_tarefa:
            return tarefa

    return None


# ==============================
# CADASTRAR TAREFA
# ==============================

def cadastrar_tarefa():
    print("\n===== CADASTRAR TAREFA =====")

    titulo = validar_texto("Título: ")
    descricao = validar_texto("Descrição: ")
    prioridade = validar_prioridade()

    if len(tarefas) == 0:
        novo_id = 1
    else:
        maior_id = 0

        for tarefa in tarefas:
            if tarefa["id"] > maior_id:
                maior_id = tarefa["id"]

        novo_id = maior_id + 1

    nova_tarefa = {
        "id": novo_id,
        "titulo": titulo,
        "descricao": descricao,
        "prioridade": prioridade
    }

    tarefas.append(nova_tarefa)

    print("\nTarefa cadastrada com sucesso!")
    print("ID da tarefa:", novo_id)


# ==============================
# EDITAR TAREFA
# ==============================

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
    novo_titulo = input("Novo título: ")

    if novo_titulo != "":
        tarefa["titulo"] = novo_titulo

    print("Descrição atual:", tarefa["descricao"])
    nova_descricao = input("Nova descrição: ")

    if nova_descricao != "":
        tarefa["descricao"] = nova_descricao

    print("Prioridade atual:", tarefa["prioridade"])

    while True:
        nova_prioridade = input(
            "Nova prioridade (Baixa, Média ou Alta): "
        )

        if nova_prioridade == "":
            break

        if nova_prioridade == "Baixa" or nova_prioridade == "Média" or nova_prioridade == "Alta":
            tarefa["prioridade"] = nova_prioridade
            break
        else:
            print("Erro: prioridade inválida.")

    print("\nTarefa atualizada com sucesso!")


# ==============================
# EXCLUIR TAREFA
# ==============================

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

    confirmacao = input(
        "Deseja realmente excluir esta tarefa? (S/N): "
    )

    if confirmacao == "S":
        tarefas.remove(tarefa)
        print("Tarefa excluída com sucesso!")

    elif confirmacao == "N":
        print("Exclusão cancelada.")

    else:
        print("Opção inválida. Exclusão cancelada.")
