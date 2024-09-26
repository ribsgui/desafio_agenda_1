class Contato:
    def __init__(self, name, number, email):
        self.name = name
        self.number = number
        self. email = email
        self.fav = False
        
    def mark_fav(self):
        if self.fav == False:
            self.fav = True
        else:
            self.fav == False
    
    def __str__(self) -> str:
        return f'Nome: {self.name},\n Telefone: {self.number},\n Email: {self.email},\n Favorito? {self.fav}'
        