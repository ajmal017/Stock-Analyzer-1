import plotly.graph_objects as go
import pandas as pd
import yfinance as yf


class candlestick:
    '''
    Build class to make a candlestick graph.
    Candlestick graphs are great tools for performing technical analysis.
    '''

    def __init__(self, ticker):
        ticker = ticker
        self.info = yf.Ticker(str(ticker)).info

    # Gets historical data for the selected stock
    def history(self, ticker):
        return yf.Ticker(str(ticker)).history(period='5y')

    # Creates candlestick chart in the form of a Plotly graph
    def graph(self, ticker):
        stockdata = self.history(ticker)
        fig = go.Figure(data=[go.Candlestick(x=stockdata.index,
                                             open=stockdata['Open'],
                                             high=stockdata['High'],
                                             low=stockdata['Low'],
                                             close=stockdata['Close'],
                                             name = 'Candlesticks')])


        fig.add_trace(go.Scatter(x=stockdata.index, y=stockdata['Close'].rolling(10).mean(), name = 'Rolling Average-10 Days',
                                 line=dict(color='white', width=2)))

        fig.add_trace(go.Scatter(x=stockdata.index, y=stockdata['Close'].rolling(30).mean(), name = 'Rolling Average-30 Days',
                                 line=dict(color='#003300', width=2)))

        fig.add_trace(go.Scatter(x=stockdata.index, y=stockdata['Close'].rolling(60).mean(), name = 'Rolling Average-60 Days',
                                 line=dict(color='blue', width=2)))

        fig.update_layout(title=str(ticker) + '\'s Candlestick Chart',
                          xaxis_title='Date',
                          yaxis_title='USD',
                          template='plotly_dark')
        graph = fig.show()
        return graph
