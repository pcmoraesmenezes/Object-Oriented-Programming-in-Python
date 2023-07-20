from dataclasses import dataclass, field

@dataclass#(init=False)
class Pessoa:
    nome: str = field(
        default='MISSING', repr=False
    )
    sobrenome: str = 'Not sent'
    idade: int = 100
    enderecos: list[str] = field(default_factory=list)
    # def __init__(self,nome,sobrenome):
    #     self.nome = nome 
    #     self.sobrenome = sobrenome
    #     self.nome_completo = f'{self.nome} {self.sobrenome}'
        

    # def __post_init__(self):
    #     print('Executado após o init')    

    # @property
    # def nome_completo(self):
    #     return f'{self.nome}, {self.sobrenome}'
    
    # @nome_completo.setter
    # def nome_completo(self, value):
    #     nome, *sobrenome = value.split()
    #     self.nome = nome
    #     self.sobrenome = ''.join(sobrenome)
    

if __name__ == '__main__':
    p1 = Pessoa()
    # print(fields(p1))
    print(p1)