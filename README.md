# caio_investment_portfolio

# Otimização de Carteira Baseada no Problema da Mochila

## Objetivo
Maximizar o retorno esperado de uma carteira de ativos financeiros, respeitando um limite de risco aceitável.

## Abordagem
Usamos uma adaptação do problema da mochila para definir os ativos (itens) e o risco (capacidade da mochila), maximizando o retorno total da carteira.

## Instalação
Instale as bibliotecas necessárias com:
```bash
pip install numpy pandas scipy matplotlib seaborn yfinance
----------------------------------------------------------------------------------------------------------------------------
Visualização dos Resultados
O projeto inclui várias visualizações gráficas para facilitar a análise dos resultados da otimização da carteira de investimentos. Utilizamos bibliotecas de visualização como Matplotlib, Seaborn, e Plotly para criar gráficos interativos e informativos, proporcionando uma visão clara do desempenho da carteira. Abaixo estão os gráficos gerados e suas descrições.

1. Fronteira Eficiente (Retorno x Risco)
Este gráfico mostra a Fronteira Eficiente, que é o conjunto de carteiras com o melhor equilíbrio entre risco e retorno. Cada ponto no gráfico representa uma carteira otimizada. A relação entre o risco (medido pela volatilidade) e o retorno esperado é traçada, permitindo identificar as carteiras com melhor desempenho relativo.

Exemplo de visualização:
Eixo X: Risco (Volatilidade)
Eixo Y: Retorno Esperado
python
Copy code
def plot_efficient_frontier(risks, returns):
    # Gráfico gerado
    plt.scatter(risks, returns)
Este gráfico ajuda os investidores a entenderem as opções disponíveis para maximizar o retorno, dado um nível de risco aceitável.

2. Alocação de Ativos
Um gráfico de Pizza (ou de Barras) é utilizado para visualizar a distribuição dos ativos na carteira. Mostra os pesos de cada ativo em porcentagem, o que ajuda a identificar a diversificação da carteira.

Exemplo de visualização:
O gráfico de pizza exibe o percentual de cada ativo na carteira.
python
Copy code
def plot_asset_allocation(weights, asset_labels):
    # Gráfico de pizza gerado
    plt.pie(weights, labels=asset_labels)
Este gráfico oferece uma visualização clara da alocação de capital em diferentes ativos e sua diversificação.

3. Histórico de Desempenho da Carteira
Este gráfico de linha mostra a evolução do retorno e do risco da carteira ao longo do tempo. Ele ajuda a monitorar como o desempenho da carteira mudou durante o período de análise, oferecendo uma visão dinâmica da performance da carteira.

Exemplo de visualização:
Eixo X: Datas
Eixo Y: Retorno e Risco (em escalas separadas)
python
Copy code
def plot_portfolio_performance(dates, portfolio_returns, portfolio_risks):
    # Gráfico de linha gerado para retorno e risco
    plt.plot(dates, portfolio_returns)
    plt.plot(dates, portfolio_risks)
