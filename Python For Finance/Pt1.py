import yfinance as yf
import datetime as dt
from pandas_datareader import data as pdr

yf.pdr_override()

stock = input("請輸入股票代號: ")+".TW"
startyear = int(input("請輸入起始年份: "))
startmonth = int(input("請輸入起始月份: "))
startday = int(input("請輸入起始日期: "))

start = dt.datetime(startyear, startmonth, startday)
now = dt.datetime.now()

df = pdr.get_data_yahoo(stock, start, now)
print(df)
