from contextlib import contextmanager

@contextmanager
def my_open(caminho, modo):
    try:
        print('Abrindo arquivo: ')
        arquivo = open(caminho,modo,encoding='utf-8')
        yield arquivo
    except Exception as error:
        print('Ocorreu um erro: ',error)
    finally:
        print('Fechando arquivo:')
        arquivo.close()

with my_open('contextlib.txt', 'w') as arquivo:
    arquivo.write('Linha 1\n')
    arquivo.write('Linha 1\n', 123)
    arquivo.write('Linha 1\n')