import abc 

class Conta(abc.ABC):
    def __init__(self, agencia: int, conta: int, saldo: float):
        self.agencia = agencia 
        self.conta = conta 
        self.saldo = saldo 

    @abc.abstractmethod
    def sacar(self, valor: float) -> float:
        pass

    def depositar(self, valor: float) -> float :
        self.saldo += valor
        self.mensagem('deposito', valor)
        return self.saldo

    def mensagem(self, msg: str='', valor: float=0) -> None:
        if msg == 'deposito':
            print(f'Realizando operação de deposito, valor depositado: {valor}, saldo atual de: {self.saldo}')
        elif msg == 'sacar':
            print(f'Realizando a operação de saque, valor sacado é de {valor}, saldo atual de: {self.saldo}')
        elif msg == 'saque_negado':
            print(f'Não foi possivel realizar a operação de saque, saque desejado: {valor}, saldo atual {self.saldo}')
        elif msg == 'limite_extra':
            print(f'Saldo insuficiente para realizar a operação de saque, entretanto utilizando o limite extra é possível realizar o saque, deseja prosseguir? para prosseguir digite (1) para cancelar operação digite (2)')

class ContaPoupanca(Conta):
    def sacar(self,valor: float):
        aux = self.saldo - valor
        if aux >= 0:
            self.saldo -= valor
            self.mensagem('sacar', valor)
            return self.saldo
        self.mensagem('saque_negado', valor)    

class ContaCorrente(Conta):
    def __init__(self, agencia: int,conta: int ,saldo: int , limite_extra: int):
        super().__init__(agencia,conta,saldo)
        self.limite_extra = limite_extra
    
    def sacar(self, valor: float):
        aux = self.saldo - valor
        if aux >= 0:
            self.saldo -= valor
            self.mensagem('sacar', valor )
            return self.saldo
        elif aux < 0 and self.limite_extra >= abs(aux):
            self.mensagem('limite_extra')
            aux2 = input()
            if aux2 == '1':
                self.saldo = - self.limite_extra 
                self.mensagem('sacar', valor)
                return self.saldo 
        else:
            self.mensagem('saque_negado', valor)


    