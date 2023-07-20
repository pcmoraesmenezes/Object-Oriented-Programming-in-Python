class Veiculo:
    total_veiculo = 0

    def __init__(self):
        Veiculo.total_veiculo +=1

    @classmethod
    def contar_veiculos(cls):
        return cls.total_veiculo
    
veiculo1 = Veiculo()
veiculo1 = Veiculo()
veiculo1 = Veiculo()
veiculo1 = Veiculo()
veiculo1 = Veiculo()
veiculo1 = Veiculo()
veiculo1 = Veiculo()
print(veiculo1.total_veiculo)
    