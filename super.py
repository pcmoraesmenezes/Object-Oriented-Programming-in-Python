class Pai():
    def __init__(self, nome):
        self.nome = nome

    def saudar(self):
        print( f'Olá eu me chamo {self.nome} ')

class Filho(Pai):
    def __init__(self,nome,idade):
        super().__init__(nome)
        self.idade = idade

    def Idade(self):
        print( f'{self.nome}, tenho {self.idade} anos')

objeto = Filho('Paulo César', 19)

objeto.Idade()