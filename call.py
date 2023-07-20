from typing import Any


class CallMe:
    def __init__(self, numero):
        self.numero = numero 
    
    def __call__(self, nome):
        print(nome, 'está chamando', self.numero)

call1 = CallMe(3182371238)
call1('pczin')