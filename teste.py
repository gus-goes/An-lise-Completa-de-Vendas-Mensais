import json
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

with open('dados.json', 'r') as arquivo:
    dados = json.load(arquivo)

# Criando um DataFrame Pandas para facilitar a manipulação
df = pd.DataFrame(dados)

# Calculando métricas adicionais
df['valor'] = df['valor'].astype(float)  # Convertendo a coluna 'valor' para float
df['dia'] = df['dia'].astype(int)  # Convertendo a coluna 'dia' para int
df['desvio_da_media'] = df['valor'] - df['valor'].mean()

# Visualizações
plt.figure(figsize=(12, 6))
plt.plot(df['dia'], df['valor'])
plt.xlabel('Dia')
plt.ylabel('Faturamento')
plt.title('Faturamento Mensal')
plt.grid(True)
plt.show()

# Box plot
plt.boxplot(df['valor'])
plt.title('Box plot do Faturamento')
plt.ylabel('Faturamento')
plt.show()

# Histograma
plt.hist(df['valor'], bins=10)
plt.xlabel('Faturamento')
plt.ylabel('Frequência')
plt.title('Histograma do Faturamento')
plt.show()