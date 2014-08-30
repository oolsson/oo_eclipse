import pandas.io.sql as sql
import MySQLdb as mdb
import pandas as pd
from pandas.tseries.offsets import Hour, Minute
import numpy as np
randn = np.random.randn
from pandas import *

con = mdb.connect('localhost', "root","MySQLoo","test2");
df=sql.read_frame('select * from prices where ticker = "ZC   MAY 13" and dt>"2013-04-02 01:30:00" and dt<="2013-04-03 01:34:00" ', con)
df.index = df['dt']
del df['dt']
del df['ticker']
#print type(df['open']['2013-03-13 18:51:00'])  #have to change db, this one is strings
#print df.to_string()
#print '-------------------------------------------------------------------------'
#print df['open'].resample('30min', how='ohlc')
#
#newts = pd.Panel(dict((col, df[col].resample('340Min', how='ohlc'))
#                      for col in df.columns))
##print newts['open']['open']
#
#
#print '-------------------------------------------------------------------------'
#df2= newts['open']['open']
#df3=newts['high']['high']
#df4=newts['low']['low']
#df5=newts['close']['close']
#d ={'open' : df2,'high' : df3,'low' : df4,'close' : df5}
#df6 = pd.DataFrame(d,columns=['open', 'high', 'low', 'close'])
#
##df4=pd.DataFrame(df2)
#print type(df6)
#print df6
#
#print 'meg--------------------'
##print pd.merge(df4, df3)

def df_ohlc_resample(df,timefreq):
    newts = pd.Panel(dict((col, df[col].resample(timefreq, how='ohlc'))
                      for col in df.columns))
    d ={'open' : newts['open']['open'],'high' : newts['high']['high'],
        'low' : newts['low']['low'],'close' : newts['close']['close']}
    df6 = pd.DataFrame(d,columns=['open', 'high', 'low', 'close'])
    return df6

def graintrading(OHLC, dr,xxx):
    bias = ['neutral']
    pullbackbars = [0]
    targetentry = ['n/a']
    barrange = ['n/a']
    
    #WE CAN ADD TWO COLUMNS WHICH ARE PROFIT TARGET AND STOP
    i=1
    while i  < len(OHLC['high']):
        #CALCULATE ENTRIES,PROFIT TARGETS AND STOPS
        if OHLC['high'][0:i].max() < OHLC['high'].ix[i]:
            bias.append('Long Bias')
        elif OHLC['low'][0:i].min() > OHLC['low'].ix[i]:
            bias.append('Short Bias')
        else:
            bias.append(bias[i-1])
    
        #CALCULATE PULLBACKBARS
        if bias[i] == 'Long Bias':
            if OHLC['high'][0:i].max() > OHLC['high'].ix[i]:
                pullbackbars.append(pullbackbars[i-1]+1)
                targetentry.append(OHLC['high'][0:i].max())
                barrange.append(OHLC['high'][0:i].max() - OHLC['low'][0:i].min())
            elif OHLC['high'][0:i].max() == OHLC['high'].ix[i]:
                pullbackbars.append(pullbackbars[i-1])
                targetentry.append(OHLC['high'][0:i].max())
                barrange.append(OHLC['high'][0:i].max() - OHLC['low'][0:i].min())
            elif OHLC['high'][0:i].max() < OHLC['high'].ix[i]:
                pullbackbars.append(0)
                targetentry.append('n/a')
                barrange.append('n/a')
            else:
                pullbackbars.append(0)
                targetentry.append('n/a')
                barrange.append('n/a')
    
    
        elif bias[i] == 'Short Bias':
            if OHLC['low'][0:i].min() < OHLC['low'].ix[i]:
                pullbackbars.append(pullbackbars[i-1]+1)
                targetentry.append(OHLC['low'][0:i].min())
                barrange.append(OHLC['high'][0:i].max() - OHLC['low'][0:i].min())
    
    
            elif OHLC['low'][0:i].min() == OHLC['low'].ix[i]:
                pullbackbars.append(pullbackbars[i-1])
                targetentry.append(OHLC['low'][0:i].min())
                barrange.append(OHLC['high'][0:i].max() - OHLC['low'][0:i].min())
    
            elif OHLC['low'][0:i].min() > OHLC['low'].ix[i]:
                pullbackbars.append(0)
                targetentry.append('n/a')
                barrange.append('n/a')
    
            else:
                pullbackbars.append(0)
                targetentry.append('n/a')
                barrange.append('n/a')
    
        else: 
            pullbackbars.append(0)
            targetentry.append('n/a')
            barrange.append('n/a')
        i= i+1
    print len(bias)
    bias = Series(bias, index = dr, name = 'Bias')
    targetentry = Series(targetentry, index = dr, name = 'TargetEntry')
    barrange = Series(barrange, index = dr, name = 'BarRange')
    pullbackbars = Series(pullbackbars, index = dr, name = 'PullBackBars')
    
    
    OHLC = OHLC.join(bias)
    OHLC = OHLC.join(pullbackbars)
    OHLC = OHLC.join(targetentry)
    OHLC = OHLC.join(barrange)
    print OHLC.to_string()
    print '----------------'
    print xxx
    print xxx % 2
    if len(OHLC)>1:
        if xxx % 2 ==1:
            return (OHLC['Bias'].ix[-2],OHLC['TargetEntry'].ix[-2],OHLC['BarRange'].ix[-2],OHLC['PullBackBars'].ix[-2])
        else:
            return (OHLC['Bias'].ix[-1],OHLC['TargetEntry'].ix[-1],OHLC['BarRange'].ix[-1],OHLC['PullBackBars'].ix[-1])
    else:
        return (OHLC['Bias'].ix[-1],OHLC['TargetEntry'].ix[-1],OHLC['BarRange'].ix[-1],OHLC['PullBackBars'].ix[-1])
    
OHLC= df_ohlc_resample(df,'2min')
dr = OHLC.index
print df.to_string()
print OHLC
print graintrading(OHLC, dr,len(df))





