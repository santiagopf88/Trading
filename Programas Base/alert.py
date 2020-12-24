import os
from dotenv import load_dotenv
import smtplib
import imghdr
from email.message import EmailMessage

import yfinance as yf
import datetime as dt
import pandas as pd
from pandas_datareader import data as pdr

load_dotenv()

EMAIL_ADDRESS=os.getenv("EMAIL_ADDRESS")
EMAIL_PASSWORD=os.getenv("EMAIL_PASSWORD")


msg=EmailMessage()

yf.pdr_override()

start=dt.datetime(2020,1,1)
now = dt.datetime.now()

stock=input("enter a stock ticker symbol: ")
print(stock)

TargetPrice=input("enter a target price: ")

msg["Subject"]="ALERT ON "+stock
msg["From"]=EMAIL_ADDRESS
msg["To"]=EMAIL_ADDRESS
alerted=False

while 1:
    df=pdr.get_data_yahoo(stock,start,now)
    currentClose=df["Adj Close"][-1]
    # print(currentClose)
    condition=currentClose>float(TargetPrice)
    if condition and alerted==False:
        alerted=True

        message=stock+" HAS ACTIVATED AN ALERT, THE PRICE IS: "+str(currentClose)

        msg.set_content(message)

        with smtplib.SMTP_SSL('smtp.gmail.com',465) as smtp:
            smtp.login(EMAIL_ADDRESS,EMAIL_PASSWORD)
            smtp.send_message(msg)
            print("completed")