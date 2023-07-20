from abc import ABC, abstractmethod

class Notificacao(ABC):
    def __init__(self,mensagem) -> None:
        self.mensagem = mensagem 

    @abstractmethod
    def enviar(self) -> bool:
        pass


class NotificacaoEmail(Notificacao):
    def enviar(self) -> bool:
        print('Email: enviando -  ', self.mensagem)
        return True

class NotificacaoSms(Notificacao):
    def enviar(self) -> bool:
        print('E-SMS: enviando -  ', self.mensagem)
        return True


def notificar(notificacao: Notificacao):
    notificacao_enviada = notificacao.enviar()
    if notificacao_enviada:
        return 'Notificação enviada: '
    print('Notificação não enviada')

#Polimorfismo:
notifcacao_email = NotificacaoEmail('Testando email')  
notificar(notifcacao_email)

notificacao_sms = NotificacaoSms('Testando SMS')
notificar(notificacao_sms)