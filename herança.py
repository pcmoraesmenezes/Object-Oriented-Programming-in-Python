#Objetivo: deixar uma classe especifica em generica, tornando os metodos e atributos da classe pai para a classe filha

class Pessoa:
    def __init__(self,nome,sobrenome):
        self.nome = nome
        self.sobrenome = sobrenome

    def falar_classe(self):
        print(self.nome, self.sobrenome, self.__class__.__name__)

class Cliente(Pessoa): #equivalente ao extends em java
    ...

class Aluno(Pessoa):
    ...

c1 = Cliente('Paulo','César')
c1.falar_classe()

a1 = Aluno('Antonio','Brazino')
a1.falar_classe()