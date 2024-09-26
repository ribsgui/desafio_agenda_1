from models.Contato import Contato

class Agenda:
    def __init__(self):
        self.contatos = []
    
    def add_contact(self, name, number, email):
        contato = Contato(name, number, email)
        self.contatos.append(contato)
    
    def list_contact(self):
        print("\n--- SEUS CONTATOS ---")
        for contato in self.contatos:
            print(f"\n{contato}")
    
    def edit_contact(self, id, name, number, email):
        if 0 <= id < len(self.contatos):
            if name:
                self.contatos[id].name = name
            if number:
                self.contatos[id].number = number
            if email:
                self.contatos[id].email = email
    
    def change_fav(self, id):
        contato = self.contatos[id]
        if 0 <= id < len(self.contatos):
            contato.mark_fav()
            
    def list_fav(self):
        favorites = [contato for contato in self.contatos if contato.fav]
        for contato in favorites:
            print(contato)
            
    def delete_contact(self, id):
        if 0 <= id < len(self.contatos):
            self.contatos.pop(id)