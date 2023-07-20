class Matematica:
    soma = []

    @classmethod
    def somar(cls):
        resultado = 0
        for i in cls.soma:
            resultado += i
        return resultado

Matematica.soma.append(5)
Matematica.soma.append(10)
resultado = Matematica.somar()
print(resultado)
