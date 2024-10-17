import yfinance as yf

def get_data(tickers, start_date, end_date):
    data = yf.download(tickers, start=start_date, end=end_date)['Adj Close']
    returns = data.pct_change().dropna()
    return data, returns

def calculate_annual_returns(returns):
    return returns.mean() * 252

def calculate_cov_matrix(returns):
    return returns.cov() * 252