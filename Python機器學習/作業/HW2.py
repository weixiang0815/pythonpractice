# -*- coding: utf-8 -*-
"""
Created on Mon Jul 19 18:52:00 2021

@author: henry
"""

import pandas as pd
import dateutil.parser as psr
import pandas_datareader as data
import matplotlib.pyplot as plt
from sys import exit

try:
    stock = input("請輸入台灣股票名稱、或代號：")
    stock_data = pd.read_csv("TaiwanStockID.csv")

    if stock.isdigit():
        stock_ID = stock
        condition = stock_data["StockID"] == int(stock)
        stock_name = stock_data[condition].iloc[0]["StockName"]

    else:
        stock_name = stock
        condition = stock_data["StockName"] == stock_name
        stock_ID = str(stock_data[condition].iloc[0]["StockID"])

    start = psr.parse(input("請輸入查詢起始日期：")).date()
    end = psr.parse(input("請輸入查詢截止日期：")).date()

    data = data.DataReader(stock_ID + ".TW", "yahoo", start, end)

except IndexError:
    if stock.isdigit():
        print("輸入了無效的股票代號")
        print("請輸入正確的台灣股票名稱或代號")
    else:
        print("輸入了無效的股票名稱")
        print("請輸入正確的台灣股票名稱或代號")

    exit()

except ValueError:
    if start > end:
        print("起始日期 > 終止日期")
        print("請輸入正確的起始日期與終止日期")

    else:
        print("輸入了無效的股票名稱、代號或日期")
        print("請輸入正確的資訊")

    exit()

close_price = data["Close"]

plt.rcParams["font.sans-serif"] = ["Microsoft JhengHei"]
plt.rcParams["axes.unicode_minus"] = False

plt.title(stock_name + " " + str(start) + " " + "~" + " " + str(end) + " " + "收盤價")
plt.xlabel("Date")
plt.ylabel("指數")

close_price.plot(label="收盤價")
close_price.rolling(window=20).mean().plot(label="20MA")
close_price.rolling(window=60).mean().plot(label="60MA")
plt.legend(loc="best")

plt.show()
