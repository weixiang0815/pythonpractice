import pandas as pd
import numpy as np
import datetime as dt
import yfinance as yf
from pandas_datareader import data as pdr

yf.pdr_override()

stock = input("Enter a stock code: ") + ".TW"

startyear = int(input("Enter the starting year: "))
startmonth = int(input("Enter the starting month: "))
startday = int(input("Enter the starting day: "))

start = dt.datetime(startyear, startmonth, startday)
now = dt.datetime.now()

df = pdr.get_data_yahoo(stock, start, now)

ma = 50
smaString = "Sma_" + str(ma)
df[smaString] = df.iloc[:, 4].rolling(window=ma).mean()

print(df)

df = df.iloc[ma:]

numH = 0
numC = 0

for i in df.index:
    if df["Adj Close"][i] > df[smaString][i]:
        print("The Close is higher")
        numH += 1
    else:
        print("The Close is lower")
        numC += 1

print(numH)
print(numC)
