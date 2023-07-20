class pessoa:
    def __init__(self, nome, sobrenome):
        self.nome = nome 
        self.sobrenome = sobrenome

p1 = pessoa('Paulo', 'César Moraes de Menezes')
# p1.nome = 'Paulo'
# p1.sobrenome = 'César Moraes de Menezes'
print(p1.nome)
print(p1.sobrenome)

class Carro:
    def __init__(self, nome='Sei la'):
        # self.nome = 'fusca' #Hard coding - algo que foi escrito diretamente no codigo
        self.nome = nome
    def acelerar(self):
        print(f'{self.nome}, está acelerando...')
        


fusca = Carro('fusca')
fusca.acelerar()

celta = Carro(nome='celta')
celta.acelerar()

Carro.acelerar(celta)


        