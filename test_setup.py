import yfinance as yf
import pandas as pd

#check that pandas is installed and working before running this file

prices = yf.download("XIU.TO", period="5d", progress=False)

print("\nRecent XIU prices:")
print(prices.tail())