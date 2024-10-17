import data_processing as dp
import optimization as opt
import visualization as viz

# Defina os parâmetros
tickers = ['AAPL', 'MSFT', 'GOOGL', 'AMZN', 'TSLA']
start_date = '2020-01-01'
end_date = '2023-01-01'

# Coleta e Processamento de Dados
data, returns = dp.get_data(tickers, start_date, end_date)
annual_returns = dp.calculate_annual_returns(returns)
cov_matrix = dp.calculate_cov_matrix(returns)

# Otimização da Carteira
optimal_weights = opt.optimize_portfolio(annual_returns, cov_matrix)

# Visualização dos Resultados
viz.plot_efficient_frontier(optimal_weights, cov_matrix, annual_returns)
viz.plot_asset_distribution(optimal_weights, tickers)
viz.plot_returns(data)
