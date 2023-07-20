from log import LogFileMixin
class Eletronico:
    def __init__(self,nome):
        self._nome = nome
        self._estado = False

    def ligar(self):
        if not self._estado:
            self._estado = True

    def desligar(self):
        if self._estado:
            self._estado = False

class Smartphone(Eletronico, LogFileMixin):
    def ligar(self):
        super().ligar()
        if self._estado:
            msg = f'{self._nome} está ligado'
            self.log_sucess(msg)

    def desligar(self):
        super().desligar()

        if self._estado:
            msg = f'{self._nome} está desligado'
            self.log_sucess(msg)