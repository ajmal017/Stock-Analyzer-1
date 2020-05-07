from numpy import cov
import pandas as pd
import yfinance as yf
import statistics


class beta:
    '''
    Class designed to calculate the beta value of a stock against
    the S&P 500 index (ticker ^GSPC)
    Formula used: Covariance of stock daily percentage return
    to S&P 500's daily percentage return divided by the variance of
    the index's daily percentage return
    '''

    def __init__(self, ticker):
        self.ticker = ticker
        self.info = yf.Ticker(str(ticker)).info

    def info(self):
        return self.info.info

    # Gets stock historical data for the past 5 years
    def history(self, ticker):
        ticker = self.ticker
        stock_hist = yf.Ticker(str(ticker)).history(period='5y').sort_index(ascending=False)
        return stock_hist

    # Gets S&P 500 historical data for the past 5 years
    def sp500(self):
        sp500_hist = yf.Ticker('^GSPC').history(period='5y').sort_index(ascending=False)
        return sp500_hist

    # Ensures that the dates of the historical data match up accordingly
    def evening(self):
        ticker = self.ticker
        stock = self.history(ticker)
        sp500 = self.sp500()
        if len(stock) > len(sp500):
            differences = []
            for i in stock.index:
                if i not in sp500.index:
                    differences = i
            stock.drop([differences], inplace = True)
        elif len(stock) < len(sp500):
            differences = []
            for i in sp500.index:
                if i not in stock.index:
                    differences = i
            sp500.drop([differences], inplace = True)
        return stock, sp500

    # Calculates daily percentage change for the selected stock
    def stock_percent_returns(self):
        stock, sp500 = self.evening()
        stock_daily_change = []
        try:
            for i, j in enumerate(list(stock['Close'])):
                stock_daily_change.append(
                    ((j - list(stock['Close'])[i+1])/(list(stock['Close'])[i+1]))*100)
            return stock_daily_change
        except IndexError:
            return stock_daily_change

    # Calculates daily percentage change for the S&P 500
    def sp500_percent_returns(self):
        stock, sp500 = self.evening()
        sp500_daily_change = []
        try:
            for i, j in enumerate(list(sp500['Close'])):
                sp500_daily_change.append(
                    ((j - list(sp500['Close'])[i+1])/(list(sp500['Close'])[i+1]))*100)
            return sp500_daily_change
        except IndexError:
            return sp500_daily_change

    # Calculates the beta value
    def beta_calculate(self):
        ticker = self.ticker
        stock_returns = self.stock_percent_returns()
        sp500_returns = self.sp500_percent_returns()
        covariance = cov(stock_returns, sp500_returns)[0][1]
        variance = statistics.variance(sp500_returns)
        beta = covariance / variance
        return beta
