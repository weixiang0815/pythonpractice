# -*- coding: utf-8 -*-
"""
Created on Mon Jul 12 20:00:21 2021

@author: henry
"""

import pandas as pd

# In[]
Rows = ["Row1", "Row2", "Row3"]
Columns = ["Column1", "Column2"]

dfList = pd.DataFrame([[1, 2], [3, 4], [5, 6]], index=Rows, columns=Columns)
print(dfList)

dfDict = pd.DataFrame({"Column1": [1, 3, 5], "Column2": [2, 4, 6]}, index=Rows)
print(dfDict)

# In[]
dfCSV = pd.read_csv("範例原始碼＆「快樂版」函式庫/Ch03 Packages/CarSales.csv")
print(dfCSV)

print(dfCSV["Country"].mode())
print(dfCSV["Age"].median())
print(dfCSV["Salary"].mean())

# In[]
dfHTML = pd.read_html("http://www.stockq.org/market/asia.php")

asia_stocks = dfHTML[7].loc[2:, :5]
print(asia_stocks)

# In[]
dfHTML = pd.read_html("http://www.stockq.org/market/asia.php")
asia_stocks = dfHTML[7].loc[2:, :5]

print(asia_stocks.to_numpy())
print(asia_stocks.values)

# In[]
dfHTML = pd.read_html("http://www.stockq.org/market/asia.php")
stocks_table = dfHTML[7].loc[2:, [0, 1, 2, 4, 5]]

condition = stocks_table[2].astype("float64") > 0
print(stocks_table[condition])