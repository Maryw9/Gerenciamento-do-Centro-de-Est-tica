from estetica import ServicoEstetica

def exibir_menu():
    print("\n----- Menu -----")
    print("1. Cadastrar Serviço")
    print("2. Consultar Todos os Serviços")
    print("3. Deletar Serviço")
    print("4. Atualizar Serviço")
    print("5. Consultar Serviço por ID")
    print("6. Zerá os IDs dos Serviços")  # Nova opção
    print("7. Sair")

def main():
    S1 = ServicoEstetica()

    while True:
        exibir_menu()
        opcao = input("\nEscolha uma opção: ")

        if opcao == "1":
            # Cadastrar serviço
            nome = input("Informe o nome do serviço: ")
            preco = input("Informe o preço do serviço: ")
            descricao = input("Descreva o serviço: ")
            duracao = input("Informe a duração do serviço em horas: ")

            S1.inserir(nome, preco, descricao, duracao)
            print("\nServiço cadastrado com sucesso!")

        elif opcao == "2":
            # Consultar todos os serviços
            print("\nServiços cadastrados:")
            S1.consultar()

        elif opcao == "3":
            # Deletar serviço
            id = int(input("Informe o ID do serviço que deseja deletar: "))
            S1.deletar(id)

        elif opcao == "4":
            # Atualizar serviço
            id = int(input("Informe o ID do serviço que deseja atualizar: "))
            nome = input("Informe o novo nome do serviço: ")
            S1.atualizar(nome, id)

        elif opcao == "5":
            # Consultar um serviço por ID
            id = int(input("Informe o ID do serviço que deseja consultar: "))
            S1.consultarServicoIndividual(id)

        elif opcao == "6":
            # Zerar IDs dos serviços
            S1.zerar_id()  # Chama o método para zerar os IDs

        elif opcao == "7":
            # Sair do sistema
            print("Saindo do sistema...")
            break

        else:
            print("Opção inválida! Tente novamente.")

# Executa o menu
if __name__ == "__main__":
    main()