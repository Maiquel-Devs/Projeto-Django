import requests
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

# Função para calcular a variação percentual entre o topo e o fundo
def calculate_variations(prices, min_variation=10):
    top = None
    bottom = None
    variations = []
    buy_prices = []  # Lista para armazenar preços de compra (fundos)
    sell_prices = []  # Lista para armazenar preços de venda (topos)
    dates = []  # Lista para armazenar as datas

    # Data atual para cálculo de semanas atrás
    current_date = datetime.today()

    for i in range(1, len(prices)):
        # Preço atual e anterior
        current_price = prices[i][1]
        previous_price = prices[i - 1][1]
        price_date = datetime.utcfromtimestamp(prices[i][0] / 1000)  # Converter timestamp para datetime

        # Detecta um topo (preço mais alto que o anterior)
        if current_price > previous_price:
            if top is None or current_price > top:
                top = current_price
            if bottom is not None:
                # Calcula a variação percentual
                variation = (top - bottom) / bottom * 100
                if variation >= min_variation:  # Só considera variações acima do mínimo
                    variations.append(variation)
                    buy_prices.append(bottom)
                    sell_prices.append(top)
                    # Calcular semanas atrás
                    weeks_ago = (current_date - price_date).days // 7
                    dates.append(f"{price_date.strftime('%d/%m/%Y')} - {weeks_ago} semanas atrás")
                    print(f"O preço subiu de ${bottom:.2f} para ${top:.2f}, com variação de {variation:.2f}% em {price_date.strftime('%d/%m/%Y')} ({weeks_ago} semanas atrás)")
                bottom = None  # Reset para próximo fundo
        else:
            if bottom is None or current_price < bottom:
                bottom = current_price

    return variations, buy_prices, sell_prices, dates

# Função para rodar a análise de variações para diferentes períodos (1, 2 e 3 meses)
def main():
    print("Iniciando a análise de oscilações do Bitcoin...")

    # Analisando para os diferentes períodos: 1, 2 e 3 meses
    for period, days in [("1 mês", 30), ("2 meses", 60), ("3 meses", 90)]:
        print(f"\nAnalisando variações para o período de {period}...\n")
        prices = get_bitcoin_data(days)

        if prices:
            print(f"Obtendo {len(prices)} pontos de dados históricos...")
            variations, buy_prices, sell_prices, dates = calculate_variations(prices)

            if variations:
                # Calcular média de variação
                avg_variation = sum(variations) / len(variations)
                # Calcular preço médio de compra e venda
                avg_buy_price = sum(buy_prices) / len(buy_prices)
                avg_sell_price = sum(sell_prices) / len(sell_prices)
                print(f"\nA média de variação entre os topos e fundos foi de {avg_variation:.2f}%")
                print(f"Preço médio de compra: ${avg_buy_price:.2f}")
                print(f"Preço médio de venda: ${avg_sell_price:.2f}")
            else:
                print("Não foram detectadas variações significativas.")
        else:
            print("Erro ao obter os dados.")

# Executando o programa
if __name__ == "__main__":
    main()
