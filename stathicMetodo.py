#Metodo que está dentro da classe, mas não pode ser usada utilizando cls nem self
#Funções que existem dentro da sua classe

class Classe:
    @staticmethod
    def soma(x,y):
        return x+y

    #Em termos de execução esse codigo acima é o mesmo do código abaixo, a diferença é que o staticmethod envolve o metodo dentro de uma classe
def soma(x,y):
    return x+y

p1 = Classe()
print(p1.soma(2,5))
print(soma(2,5))