class Carrinho:
    def __init__(self):
        self.produtos = []

    def total(self):
        return sum([p.preco for p in self.produtos])

    def inserir_produtos(self, *produtos):
        # self.produtos.extend(produtos) #Ou
        # self.produtos += produtos #Ou
        for produto in produtos:
            self.produtos.append(produto)

    def listar_produtos(self):
        print()
        for produto in self.produtos:
            print(produto.nome, produto.preco)

class Produto:
    def __init__(self,nome,preco):
        self.nome = nome
        self.preco = preco

carrinho = Carrinho()
p1,p2 = Produto('Carteira', 35), Produto('Action Figure', 180)
carrinho.inserir_produtos(p1)
carrinho.inserir_produtos(p2)
carrinho.listar_produtos()
print(carrinho.total())
