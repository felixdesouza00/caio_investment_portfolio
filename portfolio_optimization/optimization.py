from scipy.optimize import minimize
import numpy as np

def portfolio_volatility(weights, cov_matrix):
    return np.sqrt(np.dot(weights.T, np.dot(cov_matrix, weights)))

def objective_function(weights, expected_returns, cov_matrix, risk_tolerance):
    return - (np.dot(weights, expected_returns) - risk_tolerance * portfolio_volatility(weights, cov_matrix))

def optimize_portfolio(annual_returns, cov_matrix, risk_tolerance=0.1):
    constraints = ({'type': 'eq', 'fun': lambda weights: np.sum(weights) - 1})
    bounds = tuple((0, 1) for _ in range(len(annual_returns)))

    result = minimize(objective_function, len(annual_returns) * [1. / len(annual_returns), ],
                      args=(annual_returns, cov_matrix, risk_tolerance),
                      method='SLSQP', bounds=bounds, constraints=constraints)
    return result.x