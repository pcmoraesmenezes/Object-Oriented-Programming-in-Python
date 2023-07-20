class Multiplicar:
    def __init__(self, multiplicador):
        self._multiplicador = multiplicador

    def __call__(self, func):
        def interna(*args, **kwargs):
            resultado = func(*args, **kwargs)
            return resultado
        return interna

@Multiplicar(2)
def soma(x,y):
    return x + y

somar = soma(2,3)
print(somar)