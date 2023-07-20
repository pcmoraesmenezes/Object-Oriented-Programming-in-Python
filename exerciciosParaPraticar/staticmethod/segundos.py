class Segundos:

    @staticmethod
    def converte(segundos):
        horas = segundos // 3600
        minutos =  (segundos % 3600) // 60
        segundos = segundos % 60
        return f'{horas:02d}:{minutos:02d}:{segundos:02d}'
    
tempo = Segundos.converte(6000)
print(tempo)