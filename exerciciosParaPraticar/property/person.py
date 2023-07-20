class Person:
    def __init__(self,nome,idade):
        self._nome = nome 
        self._idade = idade 
    
    @property
    def nome(self):
        return self._nome
    
    @nome.setter
    def nome(self, valor):
        self._nome = valor

    @property
    def idade(self):
        return self._idade
    
    @idade.setter
    def idade(self,valor):
        self._idade = valor

pessoa1 = Person('Paulo', 19)
print(pessoa1.nome, pessoa1.idade)

pessoa2 = Person('Rodrigo', 20)
print(pessoa2.nome, pessoa2.idade)