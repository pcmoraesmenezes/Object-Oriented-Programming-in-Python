class Temperature:
    def __init__(self, celcius):
        self._celcius = celcius

    @property
    def celcius(self):
        return self._celcius
    
    @celcius.setter
    def celcius(self, value):
        self._celcius = value 

    @property
    def converte_fihre(self):
        return (self._celcius * 9/5) + 32
    
    @property
    def converte_kelvin(self):
        return(self.celcius) + (273.15)
    
    
temperatura1 = Temperature(25)
print(temperatura1.converte_fihre,temperatura1.converte_kelvin, temperatura1.celcius)

temperatura2 = Temperature(30)
print(temperatura2.converte_fihre,temperatura2.converte_kelvin,temperatura2.celcius)
    