def my_repr(cls):
    def repr_(self):
        class_name = self.__class__.__name__
        class_dict = self.__dict__
        class_repr = f'{class_name:} ({class_dict})'
        return class_repr
    cls.__repr__ = repr_
    return cls

def meu_planeta(metodo):
    def interno(self, *args, **kwargs):
        resultado = metodo(self, *args, **kwargs)

        if 'Terra' in resultado:
            return 'Você está no planeta azul'
        return resultado
    return interno

@my_repr
class Time:
    def __init__(self, nome):
        self.nome = nome 

   
@my_repr
class Planeta:
    def __init__(self, nome):
        self.nome = nome 

    @meu_planeta
    def falar_planeta(self):
        return f'O planeta é {self.nome}'

terra = Planeta('Terra')
marte = Planeta('Marte')

portugal = Time('Portugal')
brasil = Time('Brasil') 

print(brasil)
print(portugal)
print(terra)
print(marte)
print(terra.falar_planeta())
print(marte.falar_planeta())