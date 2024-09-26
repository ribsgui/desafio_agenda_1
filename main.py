from models.Agenda import Agenda
from models.Contato import Contato

def main():
    agenda = Agenda()
    
    while True:
        print("\n--- Agenda ---")
        print("1. Adicionar Contato")
        print("2. Listar Contatos")
        print("3. Editar Contato")
        print("4. Marcar/Desmarcar Favorito")
        print("5. Listar Favoritos")
        print("6. Apagar Contato")
        print("0. Sair")
        
        option = input("\n Selecione uma opção: ")
        
        if option == '1':
            name = input("Nome: ")
            number = input("Telefone: ")
            email = input("E-mail: ")
            agenda.add_contact(name, number, email)
            
        elif option == '2':
            agenda.list_contact()
        
        elif option == '3':
            print("DEIXE EM BRANCO CASO NÃO QUEIRA ALTERAR O CAMPO.")
            id = int(input("Índice do contato para editar: "))
            name = input("Novo nome do contato: ")
            number = input("Novo número do contato: ")
            email = input("Novo e-mail do contato: ")
            agenda.edit_contact(id, name if name else None, number if number else None, email if email else None)
            print("Contato Editado com Sucesso.")
            
        elif option == '4':
            id = int(input("Índice do contato que deseja marcar como favorito: "))
            agenda.change_fav(id)
            print("Favorito atualizado com sucesso!")
            
        elif option == '5':
            agenda.list_fav()
        
        elif option == '6':
            id = int(input("Digite o índice do contato que deseja apagar: "))
            agenda.delete_contact(id)
            print("Contato deletado com sucesso.")
        
        elif option == '0':
            print ("Saindo da aplicação... ")
            break
            
        else:
            print("Opção inválida! Tente novamente.")


if __name__ == "__main__":
    main()