import yfinance as yf
import pandas as pd
import plotly.graph_objects as go
from statsmodels.tsa.arima_model import ARIMA
import pmdarima as pm
from datetime import timedelta
#from datetime import date
import datetime


class arimamodel:
    '''
    Building class to develop the LTSM model to be used in the application.
    LSTM and linear regression will be used.
    '''

    def __init__(self, ticker):
        ticker = ticker
        self.info = yf.Ticker(str(ticker)).info
        #self.stockdata = self.history(period = 'max')

        #stockdata = google.history(period = "max")
    def info(self):
        return self.info.info

    def history(self, ticker):
        return yf.Ticker(str(ticker)).history(period='max')

    def arimamodel(self, ticker):
        stockdata = self.history(ticker)
        autoarimamodel = pm.auto_arima(stockdata.Close, start_p=1, start_q=1,
                                       test='adf',       # use adftest to find optimal 'd'
                                       max_p=3,
                                       max_q=3,
                                       m=4,              # frequency of series
                                       d=None,           # let model determine 'd'
                                       seasonal=True,
                                       start_P=0,
                                       D=0,
                                       trace=True,
                                       error_action='ignore',
                                       suppress_warnings=True,
                                       stepwise=True)
        return autoarimamodel

    def futuredates(self, ticker):
        daysahead = 21
        futuredats = []
        dt = datetime.datetime.now()
        for i in range(1, daysahead + 1):
            delta = timedelta(days=i)
            my_date = dt + delta
            futuredats.append(my_date)
        return futuredats

    def arimagraph(self, ticker):
        stockdata = self.history(ticker)
        daysahead = 21
        autoarimamodel = self.arimamodel(ticker)
        futuredats = self.futuredates(ticker)
        fc, confint = autoarimamodel.predict(
            n_periods=daysahead, return_conf_int=True)

        fc_series = pd.Series(fc, index=futuredats)
        lower_series = pd.Series(confint[:, 0], index=futuredats)
        upper_series = pd.Series(confint[:, 1], index=futuredats)
        predfigarima = go.Figure()
        # Create and style traces
        predfigarima.add_trace(go.Scatter(x=stockdata.index, y=stockdata.Close, name='Actual Training Set Price',
                                          line=dict(color='#003300', width=2)))

        predfigarima.add_trace(go.Scatter(x=lower_series.index,
                                          y=lower_series, name='Lower Bound',
                                          line=dict(color='grey')))

        predfigarima.add_trace(go.Scatter(x=upper_series.index,
                                          y=upper_series, name='Upper Bound',  # fill = 'tonexty',
                                          line=dict(color='grey')))

        predfigarima.add_trace(go.Scatter(x=fc_series.index, y=fc_series, name='Future Predictions',  # fill = 'tonexty',
                                          line=dict(color='blue', width=2)))

        predfigarima.update_layout(title=str(ticker) + '\'s Stock Price Predicted by ARIMA',
                                   xaxis_title='Date',
                                   yaxis_title='USD')

        predfigarima = predfigarima.show()
        return predfigarima
