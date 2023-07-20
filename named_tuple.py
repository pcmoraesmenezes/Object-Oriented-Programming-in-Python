from collections import namedtuple

Carta = namedtuple('Carta', ['valor', 'naipe'])

as_espada = Carta('A', 'Espadas')

print(as_espada)
print(as_espada.valor)
print(as_espada.naipe)