from abc import ABC, ABCMeta, abstractmethod

#class Log(metaclass=ABCMeta)

#Ou

# class Log(ABC):
#     @abstractmethod
#     def _log(self, msg):...

#     def log_error(self,msg):
#         return self._log(f'Error: {msg}')

#     def log_sucess(self,msg):
#         return self._log(f'Sucess: {msg}')
    

# class LogPrintMixin(Log):
#     def _log(self,msg):
#         print(f'{msg} ({self.__class__.__name__})')

# l = LogPrintMixin()
# l.log_error('o')

class AbstractFoo(ABC):
    def __init__(self,name):
        self._name = None
        self.name = name 
    
    @property
    @abstractmethod
    def name(self): ... 
        

    @name.setter
    def name(self,name): ...


class Foo(AbstractFoo):
    def __init__(self,name):
        super().__init__(name)

    @property
    def name(self): 
        return self._name

    @name.setter
    def name(self,name):
        self._name = name

foo = Foo('bar')
print(foo.name)