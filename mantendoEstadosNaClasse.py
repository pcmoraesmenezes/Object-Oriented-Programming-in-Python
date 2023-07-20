class fotografar:
    def __init__ (self, nome, filmando=False):
        self.nome = nome
        self.filmando = filmando

    def filmar(self):
        if self.filmando:
            print('Já está filmando!')
            return
        print('Começando a filmar... ')
        self.filmando = True
    
    def pararDeFilmar(self):
        if not self.filmando:
            print(f'{self.nome} Não está filmando! ')
            return
        print("Parando de filmar! ")
        self.filmando = False 

        
camera1 = fotografar('Sony')
print(camera1.nome, camera1.filmando)

camera1.filmar()
camera1.filmar()
camera1.pararDeFilmar()
camera1.pararDeFilmar()

