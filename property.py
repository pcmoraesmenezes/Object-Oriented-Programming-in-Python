#Getter do modo pythonico
#É uma propriedade do objeto, é um metodo que se comporta como um atributo
#Utilizado nas seguintes situações:
    # 1 - evitar quebrar o código do cliente
    # 2 - habilitar setter
    # 3 - executar ações de se obter atributo
#Atributos que começam com um ou dois _ não devem ser usados fora da classe
class Caneta():
    def __init__(self, cor):
        self._cor = cor #Esse _ após o ponto é o equivalente ao protected ou private de java

    @property
    def cor(self):
        # print("Property: ")
        return self._cor

    # @property
    # def cor_tampa(self):
    #     return 123
    @cor.setter
    def cor(self, valor):
        print(f'caneta de cor {self._cor}, agora é ', end='')
        self._cor = valor
        print(f'{self._cor}')


caneta = Caneta('Azul')
print(caneta.cor)
caneta.cor = 'vermelho'
print(caneta.cor)
print(caneta.cor)
print(caneta.cor)
