import yfinance as yf
import pandas as pd

print('pandas version:', pd.__version__)
df = yf.download('XIU.TO', period='5d', progress=False)
print(df.tail())

