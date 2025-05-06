def main():
nome = ""
idade = 0

while True:
    print("\nMenu")
    print("1.Cadastrar usuário")
    print("2.Mostrar dados cadastrados")
    print("3.Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        nome = input("nome:")
        idade = input("Idade: ")
        print("Usuario cadastrado!")
    
    elif opcao == "2":
        if nome:
            print(f"\nNome:{nome}")
            print(f"Idade:{idade}")
        else:
            print("\nNenhum usuário cadastrado.")

    elif opcao == "3":
        print("Ecerrando o sistema...")
        break

    else:
        print("Opção inválida!")
if __name__=="__main__":
    main()
