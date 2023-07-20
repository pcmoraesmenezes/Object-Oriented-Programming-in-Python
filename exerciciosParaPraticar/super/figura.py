import math
class Figura:

    def area(self):
        print('Área do:')

class Retangulo(Figura):
    def __init__ (self, x, y):
        self._x = x 
        self._y = y 
    
    @property
    def x(self):
        return self._x
    
    @x.setter
    def x(self, value):
        self._x = value 
    
    @property 
    def y(self):
        return self._y 

    @y.setter
    def y(self, value):
        self._y = value 
    
    def area(self):
        super().area()
        print(f'{type(self).__name__} é {self._x * self._y}')

class Circle(Figura):
    def __init__(self, radius):
        self._radius = radius

    @property
    def radius(self):
        return self._radius
    
    @radius.setter
    def radius(self,value):
        self._radius = value

    def area(self):
        super().area()
        print( f'{type(self).__name__} é {((self._radius ** 2) * math.pi )}')

retangulo = Retangulo(10,20)
retangulo.area()

circulo = Circle(5)
circulo.area()
