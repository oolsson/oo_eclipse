import pandas.io.sql as sql
import MySQLdb as mdb
import pandas as pd
from pandas.tseries.offsets import Hour, Minute
import numpy as np
randn = np.random.randn
from pandas import *
import datetime as dt
from pandas.io.data import DataReader
from scipy import stats
import matplotlib.pyplot as plt

con = mdb.connect('localhost', "root","","daily_Data_Yahoo");
df=sql.read_frame("SELECT * FROM daily_Data_Yahoo.omxspi", con)

df=df.pct_change()