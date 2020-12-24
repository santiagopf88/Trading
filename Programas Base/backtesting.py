import pandas as pd
import numpy as np
import yfinance as yf
import datetime as dt
import pandas_datareader
from pandas_datareader import data as pdr

yf.pdr_override()

stock=input("enter a stock ticker symbol: ")
print(stock)

startyear =2020
startmonth = 1
startday= 1

startdate = dt.datetime(startyear,startmonth,startday)

now = dt.datetime.now()

df = pdr.get_data_yahoo(stock,startdate,now)



# ma50 = 50
# ma20 = 20

# smaString20="Sma_"+str(ma20)
# smaString50="Sma_"+str(ma50)

# df[smaString50]=df.iloc[:,4].rolling(window=ma50).mean()
# df[smaString20]=df.iloc[:,4].rolling(window=ma20).mean()

emasUsed=[3,5,8,10,12,15,30,35,40,45,50,60]

for x in emasUsed:
    ema=x
    df["Ema_"+str(ema)]=round(df.iloc[:,4].ewm(span=ema,adjust=False).mean(),2)

# print(df.tail())

smasUsed=[50,20]
pos=0
num=0
percentchange=[]

for i in df.index:
    cmin = min(df["Ema_3"][i],df["Ema_5"][i],df["Ema_8"][i],df["Ema_10"][i],df["Ema_12"][i],df["Ema_15"][i])
    cmax = max(df["Ema_30"][i],df["Ema_35"][i],df["Ema_40"][i],df["Ema_45"][i],df["Ema_50"][i],df["Ema_60"][i])


    close=df["Adj Close"][i]

    if(cmin>cmax):
        # print("RED WHITE BLUE")
        if(pos==0):
            bp=close
            pos=1
            # print("BUYING NOW AT "+str(bp))
    elif(cmin<cmax):
        # print("Blue White Red")
        if(pos==1):
            pos=0
            sp=close
            # print("Sellking at "+str(sp))
            pc=(sp/bp-1)*100
            percentchange.append(pc)
    if(num==df["Adj Close"].count()-1 and pos==1):
        pos=0
        sp=close
        # print("Sellking at "+str(sp))
        pc=(sp/bp-1)*100
        percentchange.append(pc)
    num+=1
    # print(percentchange)
gains =0 
ng =0
losses=0
nl=0
totalR=1

for y in percentchange:
    if(y>0):
        gains+=y
        ng+=1
    else:
        losses+=y
        nl+=1
    totalR=totalR*((y/100)+1)
totalR=round((totalR-1)*100,2)

if(ng>0):
    avgGain= gains/ng
    maxR=str(max(percentchange))
else:
    avgGain= 0
    maxR="undefined"

if(nl>0):
    avgLoss= losses/nl
    maxL=str(min(percentchange))
    ratio=str(-avgGain/savgLoss)
else:
    avgLoss= 0
    maxL="undefined"
    ratio="inf"

if(ng>0 or nl>0):
    battingAvg = ng/(ng+nl)
else:
    battingAvg = 0

print()
print("REsult for "+stock+" going back to "+str(df.index[0])+", Sample size "+str(ng+nl)+" trades")
print("EMA used "+str(emasUsed))
print("Batting Avg "+str(battingAvg))
print("Gain/Loss ratio: "+ratio)
print("Average Gain: "+str(avgGain))
print("Average Loss: "+str(avgLoss))
print("MAX REturn:"+ maxR)
print("MAX Loss"+maxL)
print("TOTAL RETUNR OVER "+str(ng+nl)+"trades: "+str(totalR)+"%")
print()

# df = df.iloc[ma50:]

# for i in df.index:
#     if(df[smaString50][i]<df["Adj Close"][i]):
#         print("The Close was higher")
#     else:
#         print("The Close Was Lower")
