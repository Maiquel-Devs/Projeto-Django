import requests
import mplfinance as mpf
import pandas as pd
from datetime import datetime, timedelta

# Função para pegar os dados históricos do Bitcoin
def get_bitcoin_data(days):
    url = f"https://api.coingecko.com/api/v3/coins/bitcoin/market_chart?vs_currency=usd&days={days}&interval=daily"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        return data["prices"]  # Retorna os preços históricos
    else:
        print("Erro ao obter dados")
        return []

# Função para formatar os dados em formato de DataFrame para o gráfico de velas
def format_data_for_candlestick(prices):
    # Convertendo os dados em um DataFrame
    ohlc = []
    for i in range(1, len(prices)):
        timestamp = prices[i][0] / 1000  # Convertendo timestamp para segundos
        date = datetime.utcfromtimestamp(timestamp)
        open_price = prices[i-1][1]
        close_price = prices[i][1]
        high_price = max(open_price, close_price)
        low_price = min(open_price, close_price)

        ohlc.append([date, open_price, high_price, low_price, close_price])

    df = pd.DataFrame(ohlc, columns=["Date", "Open", "High", "Low", "Close"])
    df.set_index("Date", inplace=True)
    return df

# Função principal para rodar a análise e gerar o gráfico
def main():
    print("Iniciando a análise de oscilações do Bitcoin...")

    # Analisando para os diferentes períodos: 1, 2 e 3 meses
    for period, days in [("1 mês", 30), ("2 meses", 60), ("3 meses", 90)]:
        print(f"\nAnalisando variações para o período de {period}...\n")
        prices = get_bitcoin_data(days)

        if prices:
            print(f"Obtendo {len(prices)} pontos de dados históricos...")

            # Formatando os dados para candlestick
            df = format_data_for_candlestick(prices)

            # Gerando o gráfico de candlestick
            mpf.plot(df, type='candle', style='charles', title=f'Bitcoin - {period}', ylabel='Preço (em $)', volume=False)

        else:
            print("Erro ao obter os dados.")

# Executando o programa
if __name__ == "__main__":
    main()
