from datetime import date

def data_atual():
    # data_atual = str(date.today()).split('-')
    data_atual = '2024-09-01'.split('-')
    mes_anterior = str(int(data_atual[1]) - 1)
    mes_atual = data_atual[1]

    if(int(mes_anterior) <= 9):
        mes_anterior = '0' + str(mes_anterior)
    ano = data_atual[0]

    data_mes_anterior = mes_anterior + '/' + ano
    data_mes_atual = mes_atual + '/' + ano
    return data_mes_anterior, data_mes_atual





