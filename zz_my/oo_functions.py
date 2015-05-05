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

def oo_outlier_filter(data,std_limit):
    std= data.std(0)
    for i in data.columns:
        print std[i]
        data[i][np.abs(data[i]) > std[i]*std_limit] = np.nan       
    return data.fillna(method='ffill')

def oo_uneque_sig(df):
    portsig_str=df.astype(str)
    df['sig_c']=portsig_str.iloc[:,0]
    for i in range(2,len(df.columns)):
        print i
        df['sig_c']=df['sig_c']+portsig_str.iloc[:,i-1]
#     df['sig_c']=portsig_str['sig']+portsig_str['sig2']
    return df['sig_c']
def replace_na_with_avg(df):
    f = lambda x: x*np.random.randn()
    df=df.T.fillna(df.T.mean())
    df=df.T
    df2=pd.DataFrame(np.ones_like(df),index=df.index,columns=df.columns)
#     df2=df2.applymap(f)
#     print df2.head(20)
    df=df+df2
    return df

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