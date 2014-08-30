import pandas.io.sql as sql
import MySQLdb as mdb
import pandas as pd
from pandas.tseries.offsets import Hour, Minute
import numpy as np
randn = np.random.randn

con = mdb.connect('localhost', "root","","test2");
df=sql.read_frame('select * from prices where ticker = "EUR.USD" and dt>"2013-03-13 17:51:00"', con)
df.index = df['dt']
del df['dt']
del df['ticker']
# print type(df['open']['2013-03-13 18:51:00'])  #have to change db, this one is strings
print df.to_string()
print '-------------------------------------------------------------------------'
print df['open'].resample('30min', how='ohlc')

newts = pd.Panel(dict((col, df[col].resample('340Min', how='ohlc'))
                      for col in df.columns))
#print newts['open']['open']


print '-------------------------------------------------------------------------'
df2= newts['open']['open']
df3=newts['high']['high']
df4=newts['low']['low']
df5=newts['close']['close']
d ={'open' : df2,'high' : df3,'low' : df4,'close' : df5}
df6 = pd.DataFrame(d,columns=['open', 'high', 'low', 'close'])

#df4=pd.DataFrame(df2)
print type(df6)
print df6

print 'meg--------------------'
#print pd.merge(df4, df3)

def df_ohlc_resample(df,timefreq):
    newts = pd.Panel(dict((col, df[col].resample(timefreq, how='ohlc'))
                      for col in df.columns))
    d ={'open' : newts['open']['open'],'high' : newts['high']['high'],
        'low' : newts['low']['low'],'close' : newts['close']['close']}
    df6 = pd.DataFrame(d,columns=['open', 'high', 'low', 'close'])
    return df6
    
print df_ohlc_resample(df,'30min')
print len(df_ohlc_resample(df,'30min'))

#rng = pd.date_range('1/1/2000', periods=12, freq='T')
#ts = pd.Series(np.arange(12), index=rng)
#ts=ts.resample('5min', how='ohlc')
#print ts


#index = pd.date_range('1/1/2000 12:01:01', periods=22, freq='min')
#df = pd.DataFrame(randn(22, 4), index=index,columns=['A', 'B', 'C', 'D'])
#print df
#df=df['A'].resample('5Min', how='ohlc')
#print df



