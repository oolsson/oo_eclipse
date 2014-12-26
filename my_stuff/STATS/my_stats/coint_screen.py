import pandas.io.sql as sql
import MySQLdb as mdb
import pandas as pd
from pandas.tseries.offsets import Hour, Minute
import numpy as np
import datetime as dt
from pandas.io.data import DataReader
from scipy import stats
import matplotlib.pyplot as plt
import statsmodels.api as sm
import statsmodels.tsa.stattools as st
import statsmodels as stm

def hurst(p):
    tau = []; lagvec = []
    for lag in range(2,len(p)-1):
#        print lag
        pp = np.subtract(p[lag:],p[:-lag])
        lagvec.append(lag)
        tau.append(np.sqrt(np.std(pp)))
#    print tau, lagvec
    m = np.polyfit(np.log10(lagvec),np.log10(tau),1)
#    print m
    hurst = m[0]*2
    return hurst

def adf(p):
    ad=st.adfuller(p,regression='c')
    adf=ad[1]
    return adf

def HLF(p):
    x=pd.DataFrame(np.ones((len(p), 3)),columns=['y','y_lag','y_diff'])
    x['y']=p
    x['y_lag']=x['y'].shift(1)
    x['y_diff']=x['y_lag']-x['y']
    mean_=x['y_diff'].mean()
    x['y_diff_m']=mean_
    x['y_diff_lag']=x['y_diff'].shift(1)
    x=x.dropna(axis=0, how='any')
    results = sm.OLS(x['y_diff_lag'], x['y_diff']-x['y_diff_m']).fit().params
    hlf=-np.log(2)/results[0]
#    regression = pd.stats.MovingOLS(OHLC['logGLD'], x=OHLC['logGDX'],window_type= 'rolling',window = win).beta
#    print results.summary()
#    print x.to_string()
#    print hlf
#    m = pd.ols(y = x['y_diff'], x = x['y_lag'], intercept = 0, window_type="rolling", window = 128, min_periods = 127)
#    print m.beta
    return hlf

con = mdb.connect('localhost', "root","","daily_Data_Yahoo");
df=sql.read_frame("SELECT * FROM daily_Data_Yahoo.omxspi", con)
#print df.ix[1]
#print df.ix[:, 1]
#print df.icol(1)
#print df.irow(1)

#test for cointegration
#dd=st.coint(df.icol(1), df.icol(4), regression="c")
#print dd
#df.ix[:, 1:20].plot()
#plt.show()

#adftest
s=pd.Series(df.icol(0)/df.icol(11), index=df.index).dropna()
#print s.to_string()
ss=pd.DataFrame(s)
ss['adf']=pd.rolling_apply(s, 55, adf)
ss['hurst']=pd.rolling_apply(s, 55, hurst)
ss['hlf']=pd.rolling_apply(s, 55, HLF)
#ad=st.adfuller(s,regression='c')
#print ad[1] #% that it shows stationarity to
#print hurst(s)
#HLF(s)
#result = pd.rolling_apply(s, 99, HLF)
print ss.to_string()
#print s.to_string()
s.plot()
plt.show()