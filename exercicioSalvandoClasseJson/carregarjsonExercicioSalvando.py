import json

class Pessoas:
    def __init__(self, nome, sobrenome):
        self.nome = nome
        self.sobrenome = sobrenome

CAMINHO = 'exercicio.json'

with open(CAMINHO, 'r', encoding='utf-8') as file:
    data = json.load(file)
    pessoa2 = Pessoas(**data)

print(pessoa2.nome)  # Saída: Paulo
print(pessoa2.sobrenome)  # Saída: César Moraes de Menezes
