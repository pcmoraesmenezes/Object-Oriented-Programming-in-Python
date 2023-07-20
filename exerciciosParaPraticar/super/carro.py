class Veiculo:
    def __init__(self, marca, modelo):
        self._marca = marca 
        self._modelo = modelo 

    @property
    def marca(self):
        return self._marca
    
    @marca.setter  
    def marca(self, value):
        self._marca = value

    @property
    def modelo(self):
        return self._modelo

    @modelo.setter
    def modelo(self, value):
        self._modelo = value 

class Carro(Veiculo):
    def __init__(self, marca, modelo, ano):
        super().__init__(marca, modelo)
        self._ano = ano 

    @property
    def ano(self):
        return self._ano
    
    @ano.setter
    def ano(self, value):
        self._ano = value

    def informacoes(self):
        print(f"Marca: {self.marca}, Modelo: {self.modelo}, Ano: {self.ano}")

# Testando o código
carro1 = Carro('Gol', 'Daora brabo', 1985)
carro1.informacoes()
