import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

def plot_efficient_frontier(weights, cov_matrix, annual_returns):
    plt.scatter(x=portfolio_volatility(weights, cov_matrix), y=np.dot(weights, annual_returns), c='red', marker='x')
    plt.title('Fronteira Eficiente')
    plt.xlabel('Risco (Volatilidade)')
    plt.ylabel('Retorno Esperado')
    plt.show()

def plot_asset_distribution(weights, tickers):
    fig, ax = plt.subplots()
    sns.barplot(x=tickers, y=weights, ax=ax)
    ax.set(title='Distribuição de Ativos')
    plt.show()

def plot_returns(data):
    fig, ax = plt.subplots()
    data.plot(ax=ax)
    ax.set(title='Evolução dos Retornos e Riscos', xlabel='Data', ylabel='Preço Ajustado')
    plt.show()
