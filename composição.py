class Cliente:
    def __init__(self, nome):
        self.nome = nome
        self.enderecos = []

    def inserir_endereco(self, rua , numero ):
        self.enderecos.append(Enderecos(rua,numero))

    def endereco_externo(self,endereco):
        self.enderecos.append(endereco)
    def listar_enderecos(self):
        for enderec in self.enderecos:
            print('Endereço: ',enderec.rua, enderec.numero)

    def __del__(self):
        print('Apagando: ', self.nome)



class Enderecos:
    def __init__(self, rua, numero):
        self.rua = rua
        self.numero = numero

    def __del__(self):
        print("Apagando: ", self.rua, self.numero )

cliente1 = Cliente('Paulo')
cliente1.inserir_endereco('Rua Jardim das árvores', '1152')
endereco_externo = Enderecos('Rua que será apagada depois', 'numero que será apagado só depois')
cliente1.endereco_externo(endereco_externo)
cliente1.listar_enderecos()

del cliente1
print('Aqui termina o código')