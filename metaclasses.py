#Metaclasses quase nunca são utilizadas por serem complexas demais, a principal funcionalidade e controlar a criação de uma classe, controlar o comportamento padrão de classes, etc...

def meu_repr(self):
    return f'{type(self).__name__}, ({self.__dict__})'

class Meta(type):
    def __new__(mcs, name, bases, dct):
        print('Metaclass: New')
        cls = super().__new__(mcs,name,bases,dct)
        cls.attr = 1234
        cls.__repr__ = meu_repr

        if 'falar' not in cls.__dict__ or not callable(cls.__dict__['falar']):
            raise NotImplementedError('Implemente falar')
        
        return cls
    
    def __cal__(cls, *args, **kwargs):
        instancia = super().__call__(*args, **kwargs)

        if 'nome' not in instancia.__dict__:
            raise NotImplementedError('Crie o attr nome')
        
        return instancia 
    

class Pessoa(metaclass=Meta):
    def __new__(cls, *args, **kwargs):
        print('New do Pessoa')
        instancia = super().__new__(cls)
        return instancia
    
    def __init__(self, nome):
        self.nome = nome 
        print('Init do pessoa')
        

    def falar(self):
        print('falando....')

p1 = Pessoa('Paulo')
p1.falar()