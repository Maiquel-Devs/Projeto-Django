import requests
from datetime import datetime
import pytz

def obter_dados_bitcoin():
    url = 'https://api.coingecko.com/api/v3/coins/bitcoin/market_chart'
    
    # Defina o intervalo de tempo, por exemplo, "30" dias atrás
    params = {
        'vs_currency': 'usd',
        'days': '30',  # Vamos pegar dados dos últimos 30 dias
        'interval': 'daily'
    }

    try:
        response = requests.get(url, params=params)
        response.raise_for_status()  # Verifica se houve erro na requisição

        # Pega os dados históricos
        data = response.json()

        # Pegando os preços (timestamp, preço)
        preços = data['prices']

        # Converter os timestamps para datas legíveis e organizar os preços
        dados_formatados = []
        for preco in preços:
            timestamp = preco[0] / 1000  # Converte de milissegundos para segundos
            # Utilizando a data UTC com timezone
            data_formatada = datetime.fromtimestamp(timestamp, tz=pytz.utc).strftime('%d/%m/%Y')
            valor = preco[1]
            dados_formatados.append((data_formatada, valor))

        return dados_formatados

    except requests.exceptions.RequestException as e:
        print(f'Erro ao obter os dados: {e}')
        return []

# Teste da função
dados_bitcoin = obter_dados_bitcoin()
for data, valor in dados_bitcoin:
    print(f'Data: {data}, Preço: ${valor:.2f}')
