def exibir_menu():
    print("\n" + "="*35)
    print("      SISTEMA DE CONTROLE")
    print("="*35)
    print("1 - Cadastrar item")
    print("2 - Listar itens")
    print("3 - Gerar relatório")
    print("0 - Sair")
    print("="*35)
def main():
    dados = []
    while True:
        exibir_menu()
        opcao = input("Escolha uma opção: ").strip()
        if opcao == "1":
            print("[Aviso] Funcionalidade em desenvolvimento...")
        elif opcao == "2":
            print("[Aviso] Funcionalidade em desenvolvimento...")
        elif opcao == "3":
            print("[Aviso] Funcionalidade em desenvolvimento...")
        elif opcao == "0":
            print("Encerrando o programa. Até logo!")
            break
        else:
            print("Opção inválida! Tente novamente.")
if __name__ == "__main__":
    main()