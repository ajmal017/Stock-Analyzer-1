import yfinance as yf
import pandas as pd
import plotly.graph_objects as go
from statsmodels.tsa.arima_model import ARIMA
import pmdarima as pm
from datetime import timedelta
import datetime


class arimamodel:
    '''
    Building class to develop the ARIMA model to be used in the application.
    '''

    def __init__(self, ticker):
        ticker = ticker
        self.info = yf.Ticker(str(ticker)).info

    def info(self):
        return self.info.info

    # Gets the stock historical data and ensures that no non-numerical data exists
    def history(self, ticker):
        ticker = ticker
        stock_history = yf.Ticker(str(ticker)).history(period='max')
        if stock_history.isnull().values.any():
            issues = stock_history[stock_history.isnull().values]
            issue_index = []
            for issue in issues.index:
                if issue not in issue_index:
                    issue_index.append(issue)
                    stock_history.drop([issue], inplace=True)
            return stock_history
        else:
            return stock_history

    # Builds the arima model using autoarima
    def arimamodel(self, ticker):
        stockdata = self.history(ticker)
        autoarimamodel = pm.auto_arima(stockdata.Close, start_p=1, start_q=1,
                                       test='adf',
                                       max_p=3,
                                       max_q=3,
                                       m=4,
                                       d=None,
                                       seasonal=True,
                                       start_P=0,
                                       D=0,
                                       trace=True,
                                       error_action='ignore',
                                       suppress_warnings=True,
                                       stepwise=True)
        return autoarimamodel

    # Makes stock close predictions for the next 3 weeks
    def futuredates(self, ticker):
        daysahead = 21
        futuredats = []
        dt = datetime.datetime.now()
        for i in range(1, daysahead + 1):
            delta = timedelta(days=i)
            my_date = dt + delta
            futuredats.append(my_date)
        return futuredats

    # Graphs the historical data and the future 3 weeks of predictions in a Plotly graph
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
                                          y=upper_series, name='Upper Bound',
                                          line=dict(color='grey')))

        predfigarima.add_trace(go.Scatter(x=fc_series.index, y=fc_series, name='Future Predictions',
                                          line=dict(color='blue', width=2)))

        predfigarima.update_layout(title=str(ticker) + '\'s Stock Price Predicted by ARIMA',
                                   xaxis_title='Date',
                                   yaxis_title='USD')

        predfigarima = predfigarima.show()
        return predfigarima
