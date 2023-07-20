class Conexao:
    def __init__(self, host='localhost'):
        self.host=host
        self.nome = None
        self.senha = None

    def set_nome(self,nome):
        self.nome=nome

    def set_senha(self,senha):
        self.senha=senha

    @classmethod
    def create_with_auth(cls,nome,senha):
        aux = cls()
        aux.nome = nome
        aux.senha = senha
        return aux

    @staticmethod
    def message_log():
        return print('Teste')

usuario1 = Conexao()
print(usuario1.host)
usuario1= Conexao.create_with_auth('Paulo',1234)
print(usuario1.nome,usuario1.senha)