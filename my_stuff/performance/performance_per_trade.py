from pandas.io.data import DataReader
import datetime as dt
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from time import sleep
import MySQLdb as mdb


##1-Import Data--------------------------------------------------------------------------------------------------
#con = mdb.connect('localhost', "root","MySQLoo","minutedata1");
#with con: 
#    cur = con.cursor()
#    #sql="SELECT * FROM aa"
#    sql="SELECT time,opens,highs,lows,closes FROM aa \
#    WHERE time BETWEEN '2002-10-01 02:01:00' AND '2002-10-21 03:47:00'"
#    cur.execute(sql)
#    rows = cur.fetchall()
#    dat=[]
#    v=[]
#    for row in rows:
#        dat.append(row[0])
#        v.append(list(row[1:5]))
#    v=list(v)
#    for row in v:
#        for i in range(0,len(row)):
#            row[i] = float(row[i])
#
##2 Datamanipulation----------------------------------------------------------------------------
#
#df = pd.DataFrame(v, index=dat, columns=['opens','highs','lows','closes'])
#df =  df.fillna(method = 'pad')
#df=df[['opens','closes']]
#del df['opens']
#df['Close']=df['closes']

msft = DataReader("spx",  "yahoo", start=dt.datetime(2009,1,1))
sleep(1)
del msft['Volume']
del msft['Adj Close']
del msft['Open']
del msft['Low']
del msft['High']

df= msft

print df

df['MA']=pd.rolling_mean(df['Close'], 20)
df['signal'] = (df['Close'] > df['MA'])*1
df.signal=df.signal.shift(1)
df['ret'] = df['Close'].pct_change(periods=1)
df['cum_ret']=(df['ret']*df['signal'])+1
df['cum_ret']=df['cum_ret'].cumprod(1, True)

df['cum_ret'].plot()
plt.show()

trade =list(np.zeros(1))
i=1
ii=0
while i < len(df['Close']):
    if df['signal'].ix[i] ==1:
        if df['signal'].ix[i-1]!=1:
            ii=ii+1
            pos3=ii
        else:
            pos3=ii
        trade.append(pos3)
    else:
        pos3 = 0
        trade.append(pos3)
    i=i+1
    
df['trade']=trade


daysintrade = list(np.zeros(1))
i=1
while i < len(df['Close']):
    if df['trade'].ix[i]==0:
        dt=0
        daysintrade.append(dt)
    else:
        if df['trade'].ix[i]!=df['trade'].ix[i-1]:
            dt=1
        else:
            dt=dt+1
        daysintrade.append(dt)
    i=i+1

df['daysintrade']=daysintrade
#print df.to_string()
df2=df

#this parts create an index from the old index but excludes all the indexvalues where trade =0
t2 = df[np.abs(trade) >0]
new_ind= t2.index
df2=df2.reindex(new_ind)
print df2.to_string()


df2_piv = pd.DataFrame(df2['ret'].values,index=df2[['trade','daysintrade']].values.T.tolist())

print df2_piv
df3= df2_piv.unstack(0)
df3=df3+1
#print df3.to_string()
df3=df3.cumprod()
print df3.to_string()

df3.plot()
plt.show()



#df3 = df2[['signal','ret','trade']].groupby(['trade'], sort=True).sum()
#print df3

