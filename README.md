# Stock-Analyzer

This is a stock analyzer application I developed to assist anyone interested in stock trading to learn more about stocks, assist in technical analysis, as well as fundamental analysis. I hope you enjoy this program and find it a little useful!

### Required Packages

The following packages are needed in order to run the application:
* `pip install pandas`
* `pip install numpy`
* `pip install tkinter`
* `pip install plotly`
* `pip install google`
* `pip install git+https://github.com/rodrigobercini/yfinance.git`
* `pip install sklearn`
* `pip install pmdarima`
* `pip install datetime`
* `pip3 install lxml`

### Instructions

1. Download or clone this repo to your machine.
2. Extract the folder
3. Use a Python interpreter to run the StockApp.py file
4. After a few seconds the GUI should display

### What Can You Do?

Now to get an overview of which each tab of the Stock Analyzer can do. There are six tabs in total at the moment to help you get an insight into which stocks you may be interested in investing in.


#### Stock History

*The Stock History tab allows you to see the historical stock price chart*

![image](https://user-images.githubusercontent.com/46336522/80057422-8bc43600-84f4-11ea-863f-04d879900af0.png)

1. Enter a stock ticker from either the NYSE or the NASDAQ
2. Click "Select" to open up a Marketwatch.com webpage which will display the chart of your selected stock's historical data
3. You can repeat as many times as you like to analyze the stocks you want

#### Financial Statements

*The Financial Statements tab allows you to look at financial statements*

![image](https://user-images.githubusercontent.com/46336522/80057469-ad252200-84f4-11ea-860e-518cabd85de3.png)

1. Enter a stock ticker from either the NYSE or the NASDAQ
2. If you would like a more user-friendly version of the income statement, balance sheet, and statement of cash flows for your stock
    * Select a radio button for the financial statement you want
    * Click select to open up a Marketwatch.com webpage that will display the chosen financial statement for the stock you chose
3. If you would like the raw financial statements filed with the SEC, be sure that the stock ticker is entered and click the "Get" button. The SEC's EDGAR database will be opened and you can navigate to whichever financial statement you would like.

#### Analysis

*The Analysis tab allows you to look at various points of analysis*

![image](https://user-images.githubusercontent.com/46336522/81252842-f9905780-8ff4-11ea-9f71-5def64cc2106.png)

1. Enter a stock ticker from either the NYSE or the NASDAQ
2. Click "Ok" to open up a Marketwatch.com webpage that will display various financial ratios and key indicators from analysts for the stock you chose
3. Click "Calculate Beta" to calculate the beta value between the selected stock and the S&P 500

#### Modeling

*The Modeling tab allows you to look at various developed models for future analysis.*
*WIP-Linear Regression and ARIMA models with more models to be developed and added*

![image](https://user-images.githubusercontent.com/46336522/80057577-e52c6500-84f4-11ea-8c97-52f426c5cf5b.png)

1. Enter a stock ticker from either the NYSE or the NASDAQ
2. Click "Linear Regression" to open a webpage which will display a Plotly graph showing a linear regression model for the stock you chose. Click "ARIMA" to open a webpage which will display a Plotly graph showing an ARIMA model for the stock you chose

#### Candlestick Chart

*The Candlestick Chart tab allows you to look at a candlestick chart for technical analysis*

![image](https://user-images.githubusercontent.com/46336522/80057657-173dc700-84f5-11ea-8e45-75f3812ac683.png)

1. Enter a stock ticker from either the NYSE or the NASDAQ
2. Click "Create Chart" to open a webpage which will display a Plotly candlestick chart for the stock you chose. The chart is interactive and will allow you to analyze trends over any past time period.

#### Stock News

*The Stock News tab allows you to look for stock related news*

![image](https://user-images.githubusercontent.com/46336522/80057717-4fdda080-84f5-11ea-9686-e7ac4f7fa97e.png)

1. Enter a stock ticker from either the NYSE or the NASDAQ
2. Click "Get Results" to display 10 stock related webpages from Google News
3. After a couple of seconds, a list of results will be displayed in the below box
4. Select an article from the list
5. Click "Open Article" to open the selected article in your web browser

### Support

This is an ongoing project I'm working on with more features to be added. Some features being developed include:
* A stock recommender
* Multiple models to be added to the modeling tab
* Stock ticker finder

If you have any questions, suggestions, or feature requests please email me at jmuchacode@gmail.com.

Thanks for checking out my little hobby project and best wishes! :)
