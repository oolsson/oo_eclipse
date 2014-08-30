
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


f = lambda x: float(x)
# Parameters---------------------------------------------------------
start=dt.datetime(2013, 06, 01)
end=dt.date.today()
LI3=pd.date_range(start, end, freq='D')
dt7=end-dt.timedelta(days=7)
dt30=end-dt.timedelta(days=30)
dt60=end-dt.timedelta(days=60)
dt90=end-dt.timedelta(days=90)
ind=[end,dt7,dt30,dt60,dt90]

list=['DEXUSAL','DEXUSUK']
df=pd.DataFrame(index=LI3)
for i in list:
    df2 = DataReader(i, "fred", start,end)
    df2=df2.applymap(f)
    df2=df2.ffill()
    df[i]=df2
df=df.ffill()

df=df.reindex(index=ind)
df=df.pct_change(-1)
print df.to_string()
print df.iloc[0]
# plt.subplot(111)
plt.figure();
plt.subplot(211)
df.ix[2].plot(kind='bar');
plt.axhline(0, color='k')

plt.show()

