class Ponto:
    def __init__(self, x,y):
        self.x = x
        self.y = y 
    
    def __repr__(self): #repr tem que retornar uma string
        nome_da_classe = self.__class__.__name__ # Pega o nome da classe
        nome_da_classe = type(self).__name__ # Também temos essa forma de pegar o nome da classe 
        return f'({nome_da_classe}, x:{self.x}, y:{self.y})' #repr é utilizado como forma de comunicação entre os desenvolvedores
    
    def __str__(self):
        return f'({self.x}, {self.y})' #O metodo str tem prioridade sobre o metodo repr, note que ao comenta-lo a saída será diferente, entretanto é mais comum utilizar o metodo repr pois
    #o metodo str quando não consegue encontrar uma forma de retorno ele chama o metodo repr

    def __add__(self,other): #Metodo para somar dois pontos 
        novo_x = self.x + other.x
        novo_y = self.y + other.y 
        return Ponto(novo_x, novo_y)
    
    def __gt__(self, other):
        self_compara = self.x + self.y
        other_compara = other.x + other.y
        return (self_compara > other_compara)
    
if __name__ == '__main__': #Essa verificação serve para impedir que caso o modulo seja importado em outro arquivo essa parte seja falsa e não entregue o que acontece em baixo
    ponto1 = Ponto(1,2)
    ponto2 = Ponto(3,5)
    print(ponto1)
    print(repr(ponto2)) #Note que esse código não seria exibido sem o metodo __repr__, ele iria apontar para a memoria que o objeto está
    #Como o metodo str tem prioridade sobre o metodo repr, se quisermos utilizar o metodo repr mesmo com o metodo str existindo podemos passar o metodo antes da instancia 
    ponto3 = Ponto(2,7)
    ponto4 = Ponto(-1,-5)

    print(f'{ponto3!r}') #Podemos chamar o repr assim também 
    print(f'{ponto4!s}') #Podemos chamar o str assim também 

    pontoSoma1 = ponto1 + ponto2 
    pontoSoma2 = ponto3 + ponto4
    print(pontoSoma1)
    print(pontoSoma2)

    ponto_compara1 = 'O ponto 1 é maior que o ponto 2? ', ponto1 > ponto2
    ponto_compara2 = 'O ponto 3 é maior que o ponto 4? ', ponto3 > ponto4
    print(ponto_compara1)
    print(ponto_compara2)
        