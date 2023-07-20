from contas import Conta
from pessoa import Pessoa

class Banco:
    def __init__(self, agencias: list[int] | None = None,
                 clientes: list[Pessoa] | None = None,
                 contas: list[Conta] | None = None) -> None:
        self.agencias = agencias or []
        self.clientes = clientes or []
        self.contas = contas or []

    def _checa_agencia(self, conta):
        if conta.agencia not in self.agencias:
            return False
        return True

    def _checa_cliente(self, cliente):
        if cliente not in self.clientes:
            return False
        return True

    def _checa_conta(self, conta):
        if conta not in self.contas:
            return False
        return True

    def autenticar(self, cliente, conta):
        return self._checa_agencia(conta) and \
               self._checa_cliente(cliente) and \
               self._checa_conta(conta)

    def __repr__(self) -> str:
        class_name = type(self).__name__
        attrs = f'({self.agencias!r}, {self.contas!r}, {self.clientes!r})'
        return f'{class_name}, {attrs}'
