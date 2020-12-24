import pandas as pd
import numpy as np
import yfinance as yf
import datetime as dt
import pandas_datareader
from pandas_datareader import data as pdr

yf.pdr_override()

stock=input("enter a stock ticker symbol: ")
print(stock)

startyear =2010
startmonth = 1
startday= 1

startdate = dt.datetime(startyear,startmonth,startday)

now = dt.datetime.now()
while stock!="quit":
    df = pdr.get_data_yahoo(stock,startdate,now)
    df.drop(df[df["Volume"]<1000].index,inplace=True)
    dfmonth= df.groupby(pd.Grouper(freq="M"))["High"].max()
    glDate=0
    lastGLV=0
    currentDate=""
    currentGLV=0
    for index, value in dfmonth.items():
        if(value>currentGLV):
            currentGLV=value
            currentDate=index
            counter=0
        if(value<currentGLV):
            counter=counter+1
            if(counter==3 and ((index.month!=now.month)or(index.year != now.year))):
                if(currentGLV!=lastGLV):
                    print(currentGLV)
                glDate=currentDate
                lastGLV=currentGLV
                counter=0
    print(str(lastGLV))
    stock=input("enter a stock ticker symbol: ")