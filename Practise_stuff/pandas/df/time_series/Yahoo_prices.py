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
import re
import urllib2
import time
import matplotlib.pyplot as plt



# Parameters---------------------------------------------------------
database='test'
table='sp500'
start=dt.datetime(2012, 01, 01)
end=dt.datetime.today()
LI3=pd.date_range(start, end, freq='D')

#functions--------------------
f = lambda x: float(x)


df = DataReader('SP500', "fred", start,end)
df=df.applymap(f)

#calculate average per year
annual_df = df.resample('M', how='mean')
print annual_df.to_string()

#calculate return index
df['ret'] = df['SP500'].pct_change()
df=df.reindex(columns=['SP500','ret'])
df['ri'] = (1 + df['ret']).cumprod()

# calculate monthly returns
m_returns = df['ri'].resample('BM', how='last').pct_change()
print m_returns

# turn business day into full days
df=df.resample('D')
# print df.to_string()

#plot DEC 2012 closes
plt.plot(df['SP500'].ix['2012-12'])
plt.show()



