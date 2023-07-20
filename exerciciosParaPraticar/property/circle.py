
import math
class Circle:
    def __init__(self, radius):
        self._radius = radius

    def area(self):
        return ((self._radius ** 2) * math.pi )
    
    @property
    def radius(self):
        return self._radius
    
    @radius.setter
    def radius(self,value):
        self._radius = value

    
if __name__ == '__main__':
    circle = Circle(5)
    print(circle.area())

    circle2 = Circle(10)
    print(circle2.area())
    
