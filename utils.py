from datetime import date

def data_atual():
    # Obtém a data atual e separa em ['YYYY', 'MM', 'DD']
    data_atual = str(date.today()).split('-')

    # Extrai o mês e o ano atuais
    ano_atual = int(data_atual[0])
    mes_atual = int(data_atual[1])

    # Calcula o mês anterior e ajusta o ano se necessário
    if mes_atual == 1:
        # Se for janeiro, o mês anterior é dezembro do ano anterior
        mes_anterior = 12
        ano_anterior = ano_atual - 1
    else:
        mes_anterior = mes_atual - 1
        ano_anterior = ano_atual

    # Formata os meses com dois dígitos
    mes_atual_formatado = f'{mes_atual:02d}/{ano_atual}'
    mes_anterior_formatado = f'{mes_anterior:02d}/{ano_anterior}'

    # Retorna os dois meses formatados
    return mes_anterior_formatado, mes_atual_formatado



def data_mes_anterior():
    # Data de teste (você pode substituir pelo uso de `date.today()` se necessário)
    data_atual = str(date.today()).split('-')

    # Extrai o mês e ano atuais
    ano_atual = int(data_atual[0])
    mes_atual = int(data_atual[1])

    # Calcula o mês anterior e o mês anterior ao anterior
    if mes_atual == 1:
        # Caso seja janeiro, o mês anterior é dezembro do ano anterior, e o anterior a esse é novembro do mesmo ano anterior
        mes_anterior = 12
        mes_anterior_anterior = 11
        ano_anterior = ano_atual - 1
        ano_anterior_anterior = ano_atual - 1
    elif mes_atual == 2:
        # Caso seja fevereiro, o mês anterior é janeiro, e o anterior a esse é dezembro do ano anterior
        mes_anterior = 1
        mes_anterior_anterior = 12
        ano_anterior = ano_atual
        ano_anterior_anterior = ano_atual - 1
    else:
        # Para todos os outros meses
        mes_anterior = mes_atual - 1
        mes_anterior_anterior = mes_atual - 2
        ano_anterior = ano_atual
        ano_anterior_anterior = ano_atual

    # Formata os meses com dois dígitos
    mes_anterior_formatado = f'{mes_anterior:02d}/{ano_anterior}'
    mes_anterior_anterior_formatado = f'{mes_anterior_anterior:02d}/{ano_anterior_anterior}'

    # Retorna os dois meses formatados
    return mes_anterior_anterior_formatado, mes_anterior_formatado








