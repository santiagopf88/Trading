import time as true_time
import pprint
import pathlib
import operator
import pandas as pd

from datetime import datetime
from datetime import timedelta
from configparser import ConfigParser
from pyrobot.robot import PyRobot
from pyrobot.indicators import Indicators

#Grab config file values

config=ConfigParser()
config.read("config/config.ini")

CLIENT_ID = config.get("main","CLIENT_ID")
REDIRECT_URI=config.get("main","REDIRECT_URI")
CREDENTIALS_PATH=config.get("main","JSON_PATH")
ACCOUNT_NUMBER=config.get("main","ACCOUNT_NUMBER")

#initialize robot

trading_robot=PyRobot(
    client_id=CLIENT_ID,
    redirect_uri=REDIRECT_URI,
    credentials_path= CREDENTIALS_PATH,
    trading_account=ACCOUNT_NUMBER,
    paper_trading=True
)

