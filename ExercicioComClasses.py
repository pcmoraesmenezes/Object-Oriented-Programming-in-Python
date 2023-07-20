# 1 - Crie uma classe Carro(nome)
# 2 - Crie uma classe Motor(nome)
# 3 - Crie uma classe Fabricante(nome)
# 4 - Faça a ligação entre Carro e Motor
# Obs - Um motor pode ter varios carros
# 5 - Faça a ligação entre Carro e Fabricante
# Obs - Um fabricante pode ter varios carros
# Exiba o nome do carro, motor e fabricante na tela.

class Carro:
    def __init__(self, nome, motor, fabricante):
        self.nome = nome
        self.fabricante = fabricante
        self.motor = motor

    def exibir_Carro(self):
        print(f'Carro: {self.nome}, Motor: {self.motor.nome}, Fabricante: {self.fabricante.nome}')

class Motor:
    def __init__(self, nome):
        self.nome = nome

class Fabricante:
    def __init__(self, nome):
        self.nome = nome

motor = Motor('Potente')
fabricante = Fabricante('Volkswagen')
carro = Carro('T-Cross', motor, fabricante)
carro.exibir_Carro()