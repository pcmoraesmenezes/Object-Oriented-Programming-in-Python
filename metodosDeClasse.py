#Self será substituido por cls

class Pessoa:
    ano = 2023 #Atributo de classe

    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    @classmethod
    def metodoClasse(cls):
        print("Hey")

    @classmethod
    def criar_Com_50_Anos(cls, nome):
        return cls(nome, 50)

print(Pessoa.ano)
p1 = Pessoa("Paulo", 19)
Pessoa.metodoClasse()
p2 = Pessoa.criar_Com_50_Anos("Rickson")
print(p2.nome,p2.idade)