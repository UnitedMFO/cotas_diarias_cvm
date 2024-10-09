import requests

def obter_dados_cnpj(cnpj):
    # URL da requisição que você encontrou no painel de rede
    url = "https://exemplo.com/api/dados"

    # Cabeçalhos da requisição, se necessário
    headers = {
        'User-Agent': 'Mozilla/5.0',
        'Content-Type': 'application/x-www-form-urlencoded',  # Exemplo, pode variar
    }

    # Dados que precisam ser enviados no corpo da requisição POST
    data = {
        'cnpj': cnpj,
        'outro_parametro': 'valor',  # Outros parâmetros necessários
    }

    # Fazendo a requisição POST
    response = requests.post(url, headers=headers, data=data)

    # Verificando se a requisição foi bem-sucedida
    if response.status_code == 200:
        # Retornar o conteúdo da resposta em formato JSON ou como texto
        return response.json()  # ou response.text se for HTML
    else:
        print(f"Erro na requisição: {response.status_code}")
        return None

# Exemplo de uso
dados = obter_dados_cnpj('38065069000176')
print(dados)
