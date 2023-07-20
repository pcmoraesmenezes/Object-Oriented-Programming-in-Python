class Data:
    dia_atual = 14
    mes_atual = 7
    ano_atual = 2023

    @classmethod
    def exibir_data_atual(cls):
        exibir_data_atual = f'{cls.dia_atual}/{cls.mes_atual}/{cls.ano_atual}'
        print(exibir_data_atual)
    
data = Data.exibir_data_atual()