class Animal:
    def falar(self):
        print( 'Som que o animal faz')
    
class Cachorro(Animal):
    def falar(self):
        super().falar()
        print('Au Au!')


animal1 = Cachorro()
animal1.falar()
    
    