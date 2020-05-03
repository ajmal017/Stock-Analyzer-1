from tkinter import *
from tkinter import ttk
import pandas as pd
from linearregressmodel import lrmodel
from candlestick import candlestick
import webbrowser
import googlesearch
import lxml
from arima import arimamodel
from betacalc import beta

# pulls expected ticker symbols


def gettickers():
    nysecomps = pd.read_csv(
        r'https://old.nasdaq.com/screening/companies-by-name.aspx?letter=0&exchange=nyse&render=download')
    nysecomps['Symbol'] = [i.strip() for i in nysecomps['Symbol']]
    nasdaq = pd.read_csv(
        'https://old.nasdaq.com/screening/companies-by-name.aspx?letter=0&exchange=nasdaq&render=download')
    nasdaq['Symbol'] = [i.strip() for i in nasdaq['Symbol']]
    symbolslist = list(nysecomps['Symbol']) + list(nasdaq['Symbol'])
    return symbolslist


tickers = gettickers()

# command to be executed when the button on the 'Historical Data' tab is clicked


def clicked():
    selection = str(txthistory.get()).upper()
    if selection in tickers:
        histstatuslbl.configure(text='Opening the historical data for ' + str(selection))
        yahooinfo(selection)
    else:
        histstatuslbl.configure(text='Please enter a valid NYSE  or NASDAQ ticker')


# builds the window for the executable
window = Tk()
window.title("Stock Analyzer")
window.configure(background='black')
window.geometry('600x250')

# tabs defined and built
tab_control = ttk.Notebook(window)

HistoricalData = ttk.Frame(tab_control)
FinancialStatements = ttk.Frame(tab_control)
Analysis = ttk.Frame(tab_control)
Modeling = ttk.Frame(tab_control)
CandlestickChart = ttk.Frame(tab_control)
StockNews = ttk.Frame(tab_control)

tab_control.add(HistoricalData, text='Historical Data')
tab_control.add(FinancialStatements, text='Financial Statements')
tab_control.add(Analysis, text='Analysis')
tab_control.add(Modeling, text='Modeling')
tab_control.add(CandlestickChart, text='Candlestick Chart')
tab_control.add(StockNews, text='Stock News')


'''
Stock historical data tab
'''

# text label on stock history tab
lblstockhistory = Label(HistoricalData, text="Stock Ticker:")
lblstockhistory.place(x=0, y=0)

histstatuslbl = Label(HistoricalData)
histstatuslbl.place(x=200, y=0)

# text field on stock history tab to enter the stock ticker you want
txthistory = Entry(HistoricalData, width=8)
txthistory.place(x=70, y=0)

# button on stock history tab run the clicked function to open the requested ticker historical data
btnstockhistory = Button(HistoricalData, text="Select", command=clicked)
btnstockhistory.place(x=130, y=0)

# function to open the typed stock ticker's on the history tab


def yahooinfo(selection):
    stock = str(selection)
    if stock in tickers:
        webbrowser.open('https://www.marketwatch.com/investing/stock/' +
                        str(stock).lower() + '/charts')


'''
Financial Statement tab
'''

# text label on Financial Statements tab
lblfinstates = Label(FinancialStatements, text="Stock Ticker:")
lblfinstates.place(x=0, y=0)

# text field on Financial Statements tab asking for a stock ticker to be entered
txtfinstates = Entry(FinancialStatements, width=8)
txtfinstates.place(x=70, y=0)

# variable to store the selected value
selected = IntVar()

# radio buttons to choose a financial statement
rad1 = Radiobutton(FinancialStatements, text='Income Statement', value=1, variable=selected)
rad1.place(x=0, y=20)
rad2 = Radiobutton(FinancialStatements, text='Balance Sheet', value=2, variable=selected)
rad2.place(x=130, y=20)
rad3 = Radiobutton(FinancialStatements, text='Cash Flow', value=3, variable=selected)
rad3.place(x=230, y=20)

# function to run when a radio button is selected and the button is clicked


def selectedradiobut():
    stock = str(txtfinstates.get()).upper()
    statement = selected.get()
    if stock in tickers:
        if statement == 1:
            finstatuslabel.configure(text='Opening the income statement for ' + str(stock))
            webbrowser.open('https://www.marketwatch.com/investing/stock/' +
                            str(stock).lower() + '/financials')
        elif statement == 2:
            finstatuslabel.configure(text='Opening the balance sheet for ' + str(stock))
            webbrowser.open('https://www.marketwatch.com/investing/stock/' +
                            str(stock).lower() + '/financials/balance-sheet')
        elif statement == 3:
            finstatuslabel.configure(text='Opening the cash flow statement for ' + str(stock))
            webbrowser.open('https://www.marketwatch.com/investing/stock/' +
                            str(stock).lower() + '/financials/cash-flow')
    else:
        finstatuslabel.configure(text='Please enter a valid NYSE or NASDAQ ticker')


# status update on selection
finstatuslabel = Label(FinancialStatements)
finstatuslabel.place(x=170, y=0)


# button on the financial statements tab, gets selected financial statement
btnfinstates = Button(FinancialStatements, text="Select", command=selectedradiobut)
btnfinstates.place(x=330, y=20)


def secfilings():
    secfile = str(txtfinstates.get()).upper()
    if secfile in tickers:
        webbrowser.open('https://www.sec.gov/cgi-bin/browse-edgar?CIK=' +
                        str(secfile) + '&Find=Search&owner=exclude&action=getcompany')
    else:
        lblfilingsstatus.configure(text='Please enter a valid NYSE or NASDAQ ticker')


# sec filing instructions
secfilinglabel = Label(FinancialStatements, text='Click get to open all SEC EDGAR filings')
secfilinglabel.place(x=0, y=45)

# text label updating on status of text typed
lblfilingsstatus = Label(FinancialStatements)
lblfilingsstatus.place(x=0, y=65)

# button on SEC filings tab, gets the list of all SEC filings
btnfilings = Button(FinancialStatements, text='Get', command=secfilings)
btnfilings.place(x=220, y=45)

'''
Stock analysis tab
'''

# function to run to pull analysis for a typed stock


def analysis():
    typed = txtanalysis.get().upper()
    typedstock = str(typed).upper()
    if typed in tickers:
        lblerror.configure(text='Opening analysis...')
        webbrowser.open('https://www.marketwatch.com/investing/stock/' +
                        str(typedstock).lower() + '/analystestimates')
    else:
        lblerror.configure(text='Please enter a valid NYSE or NASDAQ ticker')


# text label on the Analysis tab prompting entry of a ticker
lblanalysis = Label(Analysis, text="Get financial ratios: ")
lblanalysis.grid(column=1, row=3)

# text label on the Analysis tab updating on the status of the text typed
lblerror = Label(Analysis)
lblerror.grid(column=1, row=5)

# text field on the Analysis tab to enter the ticker of the stock you want analysis for
txtanalysis = Entry(Analysis, width=8)
txtanalysis.grid(column=2, row=3)

# function to calculate beta value of the selected stock against the S&P


def calc_beta():
    tickername = txtanalysis.get().upper()
    if tickername in tickers:
        stock = beta(tickername)
        betaval = stock.beta_calculate()
        lblbetavalue.configure(text=betaval)


# button on the Analysis tab to return MarketWatch analysis for a typed ticker
btnanalysis = Button(Analysis, text="Ok", command=analysis)
btnanalysis.grid(column=3, row=3)

# button to calculate daily calculated beta against the S&P 500
btnbetacalc = Button(Analysis, text='Calculate Beta', command=calc_beta)
btnbetacalc.grid(column=4, row=3)

lblbetavalue = Label(Analysis)
lblbetavalue.grid(column=5, row=3)

'''
Stock modeling tab
'''

# text label on the Stock Modeling tab, gives text prompt to enter ticker
lblmodel = Label(Modeling, text="Get modeling of stock: ")
lblmodel.grid(column=1, row=3)

# text field on the Stock Modeling tab to enter the ticker
txtmodel = Entry(Modeling, width=8)
txtmodel.grid(column=2, row=3)

# function to return the stock graph with linear regression results


def modelreturn():
    tickerstr = str(txtmodel.get()).upper()
    if tickerstr in tickers:
        stock = lrmodel(tickerstr)
        results = stock.graphlrresults(tickerstr)
        return results

# function to return the stock graph with arima results with 30 day horizon


def arima():
    tickerstr = str(txtmodel.get()).upper()
    if tickerstr in tickers:
        stock = arimamodel(tickerstr)
        results = stock.arimagraph(tickerstr)
        return results


# button on the Stock Modeling tab to return the linear regression model
btnmodel = Button(Modeling, text="Linear Regression Model", command=modelreturn)
btnmodel.grid(column=3, row=3)

# button on the Stock Modeling tab to return the arima model
btnarima = Button(Modeling, text='ARIMA', command=arima)
btnarima.place(x=330, y=0)


'''
Candlestick Chart tab
'''

# text label on Candlestick Chart tab asking for entry of a stock ticker
lblcandle = Label(CandlestickChart, text='Create candlestick chart for stock: ')
lblcandle.grid(column=1, row=3)

# text field on Candlestick Chart tab to enter the ticker you want a candlestick chart for
txtcandle = Entry(CandlestickChart, width=8)
txtcandle.grid(column=2, row=3)

# function to return a candlestick chart of the entered ticker


def candlechart():
    chartticker = str(txtcandle.get()).upper()
    if chartticker in tickers:
        stock = candlestick(chartticker)
        candlestickchart = stock.graph(chartticker)
        return candlestickchart


# button on Candlestick Chart tab to actually run the function and return the graph
btncandle = Button(CandlestickChart, text='Create Chart', command=candlechart)
btncandle.grid(column=3, row=3)


'''
Stock News tab
'''

# Prompt label for stock news tab asking for a stock ticker to find news
lbl_stock_search = Label(StockNews, text='Select a stock ticker to search for:')
lbl_stock_search.place(x=0, y=0)

# Textbox to open stock news
txt_stock_search = Entry(StockNews, width=8)
txt_stock_search.place(x=200, y=0)

# Function to get a list of urls for the ticker related news


def search():
    list_of_results = []
    query = str(txt_stock_search.get()).upper() + ' news'
    for j in googlesearch.search_news(query, stop=10, pause=2.0):
        list_of_results.append(j)
    counter = 1
    for i in list_of_results:
        listbox.insert(counter, list_of_results[counter - 1])
        counter += 1

# Function to open whichever article is selected


def open_selected_result():
    selected_news_art = listbox.get(ACTIVE)
    webbrowser.open(selected_news_art)


# button on stock news tab to list all 10 results
btn_stock_search = Button(StockNews, text='Get Results', command=search)
btn_stock_search.place(x=250, y=0)

# listbox of all returned urls
listbox = Listbox(StockNews)
listbox.place(x=0, y=35)


# button to pull the selected url from the list
btn_open_art = Button(StockNews, text='Open Article', command=open_selected_result)
btn_open_art.place(x=490, y=30)

#scrollbar = Scrollbar(tab6, orient = VERTICAL)
#scrollbar.config(command = listbox.yview)

listbox.configure(width=80)

'''
Builds notebook
'''

# builds the notebook
tab_control.pack(expand=1, fill='both')

# keeps the program running until exited
window.mainloop()
