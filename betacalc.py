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

    def history(self, ticker):
        ticker = self.ticker
        stock_hist = yf.Ticker(str(ticker)).history(period='5y').sort_index(ascending=False)
        return stock_hist
        # return yf.Ticker(str(ticker)).history(period='max')

    def sp500(self):
        sp500_hist = yf.Ticker('^GSPC').history(period='5y').sort_index(ascending=False)
        # return yf.Ticker('^GSPC').history(period = 'max')
        return sp500_hist

    def stock_returns(self, ticker):
        ticker = self.ticker
        days = self.history(ticker)
        stock_daily_change = []
        try:
            for i, j in enumerate(list(days['Close'])):
                stock_daily_change.append(
                    ((j - list(days['Close'])[i+1])/(list(days['Close'])[i+1]))*100)
            return stock_daily_change
        except IndexError:
            return stock_daily_change

    def sp500_returns(self):
        days = self.sp500()
        sp500_daily_change = []
        try:
            for i, j in enumerate(list(days['Close'])):
                sp500_daily_change.append(
                    ((j - list(days['Close'])[i+1])/(list(days['Close'])[i+1]))*100)
            return sp500_daily_change
        except IndexError:
            return sp500_daily_change

    def beta_calculate(self):
        ticker = self.ticker
        stock_returns = self.stock_returns(ticker)
        sp500_returns = self.sp500_returns()
        covariance = cov(stock_returns, sp500_returns)[0][1]
        variance = statistics.variance(sp500_returns)
        beta = covariance / variance
        return beta
