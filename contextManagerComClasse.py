class MyContextManager:

    def __init__(self, caminho, modo):
        self._caminho = caminho 
        self._modo = modo 
        self._arquivo = None
    
    @property
    def caminho(self):
        return self._caminho
    
    @caminho.setter
    def caminho(self, caminho):
        self._caminho = caminho
    
    @property
    def modo(self):
        return self._modo 

    @modo.setter 
    def modo(self,modo):
        self._modo = modo 
    

    def __enter__(self):
        print('Abrindo arquivo')
        self._arquivo = open(self._caminho, self._modo, encoding='utf-8')
        return self._arquivo

    def __exit__(self, class_exception, exception_,traceback_):
        print('fechando arquivo')
        self._arquivo.close()

instancia = MyContextManager('ContextManagerComClasse.txt', 'w')
with instancia as arquivo:
    arquivo.write('Linha 1\n')
    arquivo.write('Linha 2\n')
    arquivo.write('Linha 3\n')
    print('teste')