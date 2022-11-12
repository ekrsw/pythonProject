import pandas_datareader as pdr
import datetime

start = '2000-01-01'
end = datetime.date.today()
ticker = 'TSLA'

df = pdr.data.DataReader(ticker, 'yahoo', start, end)
print(df)