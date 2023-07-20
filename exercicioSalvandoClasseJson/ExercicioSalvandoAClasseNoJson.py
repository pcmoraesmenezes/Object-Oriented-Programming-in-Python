#Exercicio - Salve sua classe em json
#Salve os dados da sua classe em json e depois crie novamente as instancias da classe com os dados salvos
#Faça em arquivos separados 

import json

class Pessoas:
    def __init__ (self, nome, sobrenome):
        self.nome = nome
        self.sobrenome = sobrenome

pessoa1 = Pessoas(nome = 'Paulo', sobrenome='César Moraes de Menezes')

CAMINHO = 'exercicio.json'

with open(CAMINHO, 'w', encoding='utf-8') as file:
    json.dump(pessoa1.__dict__,file,ensure_ascii=False, indent=2)

with open(CAMINHO, 'r', encoding='utf-8') as file:
    pessoa1 = json.load(file)
    print(pessoa1)