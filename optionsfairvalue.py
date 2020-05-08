import numpy as np
import scipy.stats as si
import sympy as sy
from sympy.stats import Normal, cdf
import yfinance as yf
import statistics


class options:

    '''
    Class created to find the fair value of a non-dividend paying call or put option for a selected stocks using the Black-Scholes Model
    '''

    def __init__(self, ticker, strike, time_to_maturity, interest_rate):
        self.ticker = ticker
        self.info = yf.Ticker(str(ticker)).info
        self.strike = strike
        self.time_to_maturity = time_to_maturity
        self.interest_rate = interest_rate

    # Test Function
    def volatility(self):
        stock = yf.Ticker(self.ticker).history(period='1y').sort_index(ascending=False)
        try:
            volatilitycalc = []
            for i, j in enumerate(stock['Close']):
                volatilitycalc.append(np.log((j)/stock['Close'][i+1]))
            return statistics.stdev(volatilitycalc) * np.sqrt(len(volatilitycalc))
        except IndexError:
            return statistics.stdev(volatilitycalc) * np.sqrt(len(volatilitycalc))

    def current_market_price(self):
        market_price = yf.Ticker(str(self.ticker)).history(period='1d')['Close'][0]
        return float(market_price)

    # Test time
    def d1_test(self):
        strike, interest_rate, time_to_maturity = self.strike, self.interest_rate, self.time_to_maturity
        spot = self.current_market_price()
        volatilityval = self.volatility()
        d1 = (np.log(spot / strike) + ((time_to_maturity/365) * (interest_rate +
                                                                 ((volatilityval**2)/2)))) / (volatilityval*np.sqrt(time_to_maturity/365))
        return d1

    def d2_test(self):
        strike, interest_rate, time_to_maturity = self.strike, self.interest_rate, self.time_to_maturity
        spot = self.current_market_price()
        volatilityval = self.volatility()
        d2 = self.d1_test() - (volatilityval * np.sqrt(time_to_maturity/365))
        return d2

    def call_price(self):
        strike, interest_rate, time_to_maturity = self.strike, self.interest_rate, self.time_to_maturity
        spot = self.current_market_price()
        return round((spot * si.norm.cdf(self.d1_test(), 0.0, 1.0) - strike * np.exp(-(interest_rate) * time_to_maturity/365) * si.norm.cdf(self.d2_test(), 0.0, 1.0)),2)

    def put_price(self):
        strike, interest_rate, time_to_maturity = self.strike, self.interest_rate, self.time_to_maturity
        spot = self.current_market_price()
        return round((strike * np.exp(-(interest_rate) * time_to_maturity/365) * si.norm.cdf(-(self.d2_test())) - spot * si.norm.cdf(-(self.d1_test()))),2)

op = options('GOOG', 1390, 5, 0.05)
print(op.volatility())
