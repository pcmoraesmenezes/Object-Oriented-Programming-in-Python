class Autor:
    def __init__(self, nome):
        self.nome = nome

    def exibir_autor(self):
        return print(f'Autor: {self.nome}')

class Livro:
    def __init__(self,titulo,autor):
        self.titulo = titulo
        self.autor = autor

    def exibir_Livro(self):
        print(f'Livro: {self.titulo}')
        return self.autor.exibir_autor()

autor = Autor('Hal Elrod')

livro = Livro('O milagre do Amanhã', autor)

livro.exibir_Livro()

