import matplotlib.pyplot as plt
import numpy as np

# Dados de preços e variações
dados = {
    "1 mês": {
        "compras": [78783.94, 81098.90],
        "vendas": [94261.53, 94261.53],
        "datas": ["21/03/2025", "20/03/2025"],
        "variacao_percentual": [19.65, 16.23]
    },
    "2 meses": {
        "compras": [86000.00, 87000.00],
        "vendas": [90000.00, 90000.00],
        "datas": ["15/02/2025", "14/02/2025"],
        "variacao_percentual": [4.65, 3.45]
    },
    "3 meses": {
        "compras": [78000.00, 80000.00],
        "vendas": [83000.00, 85000.00],
        "datas": ["12/01/2025", "11/01/2025"],
        "variacao_percentual": [6.41, 6.25]
    }
}

# Criar gráfico de área
plt.figure(figsize=(10, 6))

# Plotar área para os preços de compra e venda
for i, (periodo, info) in enumerate(dados.items()):
    plt.fill_between(info["datas"], info["compras"], color='blue', alpha=0.3, label=f'Compra - {periodo}')
    plt.fill_between(info["datas"], info["vendas"], color='red', alpha=0.3, label=f'Venda - {periodo}')

# Ajustando os detalhes do gráfico
plt.title('Variações de Preço do Bitcoin (Gráfico de Área)', fontsize=14)
plt.xlabel('Data', fontsize=12)
plt.ylabel('Preço (em $)', fontsize=12)
plt.xticks(rotation=45)
plt.legend()

# Exibir o gráfico
plt.tight_layout()
plt.show()
