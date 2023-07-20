class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    @property
    def width(self):
        return self._width
    
    @width.setter
    def width(self, value):
        if value < 0:
            print('You must give a positive number. I"ll convert it to a positive value.')
            self._width = abs(value)
        else:
            self._width = value

    @property
    def height(self):
        return self._height
    
    @height.setter
    def height(self, value):
        if value < 0:
            print('You must give a positive number. I"ll convert it to a positive value.')
            self._height = abs(value)
        else:
            self._height = value 

    @property
    def area(self):
        return self._width * self._height

a1 = Rectangle(-10, -15)
print(a1.width)  # Output: 10
print(a1.height)
print(a1.area)
