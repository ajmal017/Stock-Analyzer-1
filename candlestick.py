import plotly.graph_objects as go
import pandas as pd
from datetime import datetime
import yfinance as yf


class candlestick:
    '''
    Build class to make a candlestick graph.
    Candlestick graphs are great tools for performing technical analysis.abs
    '''

    def __init__(self, ticker):
        ticker = ticker
        self.info = yf.Ticker(str(ticker)).info

    def history(self, ticker):
        return yf.Ticker(str(ticker)).history(period='max')

    def graph(self, ticker):
        stockdata = self.history(ticker)
        fig = go.Figure(data=[go.Candlestick(x=stockdata.index,
                                             open=stockdata['Open'],
                                             high=stockdata['High'],
                                             low=stockdata['Low'],
                                             close=stockdata['Close'])])
        fig.update_layout(title=str(ticker) + '\'s Candlestick Chart',
                          xaxis_title='Date',
                          yaxis_title='USD')
        graph = fig.show()
        return graph
