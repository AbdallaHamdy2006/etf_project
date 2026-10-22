import yfinance as yf
import pandas as pd
import os

#using XIU and XBB as examples 

TICKERS = ['XIU.TO', 'XBB.TO']   # equity index ETF, bond ETF
START, END = '2019-06-01', '2021-06-30'

for t in TICKERS:
    raw = yf.download(t, start=START, end=END, auto_adjust=False, progress=False)
    close = raw['Close']
    if isinstance(close, pd.DataFrame):   # newer yfinance returns a table
        close = close.iloc[:, 0]
    close.name = 'price'
    close.to_csv('data/' + t.replace('.', '_') + '_price.csv')
    print(t, len(close), 'rows saved')

     