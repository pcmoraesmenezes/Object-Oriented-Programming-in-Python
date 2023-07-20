import math 

class Circunferencia:
    pi = math.pi 

    @classmethod
    def circunferencia(cls,raio):
        circunferencia = 2 * cls.pi * raio 
        return circunferencia
    
area1 = Circunferencia.circunferencia(10)
print(area1)