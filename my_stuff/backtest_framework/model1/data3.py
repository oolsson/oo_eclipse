import pandas.io.sql as sql
import MySQLdb as mdb
import pandas as pd
from pandas.tseries.offsets import Hour, Minute
import numpy as np
randn = np.random.randn
from pandas import *
import datetime as dt
from pandas.io.data import DataReader
import zz_my.oo_perf as op
import zz_my.oo_functions  as of
from dateutil import parser
import time
import datetime
import matplotlib.pyplot as plt


f = lambda x: float(x)
l = lambda x: np.log(x)


buckets=49


# get universe
con = mdb.connect('localhost', "root","","test");
sqll="SELECT ticker FROM test.index_constit where indexx = 'SP500' and ticker like 'a%';"
# sqll="SELECT ticker FROM test.index_constit where indexx = 'SP500';"
tick_list=sql.read_frame(sqll, con)
tick_list=list(tick_list['ticker'])
print tick_list
print len(tick_list)

con = mdb.connect('localhost', "root","","test");

#price data-----------------------------------------------------------------------------------------
ii=0
for i in tick_list:
    sqll2="SELECT Adj_Close,date FROM test.yahoo_p where ticker = '%s' and date >'2007';" %(i)
    x=sql.read_frame(sqll2, con,'date',parse_dates=['date'])
    if ii==0:
        dfp=x
        dfp.columns=[i]
    else:
        dfp[i]=x['Adj_Close']
    ii +=1
ret=dfp.applymap(f).pct_change(1)
dfp=dfp.applymap(f)
# print dfp['YHOO'].tail(3)

#sig data-----------------------------------------------------------------------------
df=pd.DataFrame()
df1=pd.DataFrame(index=df.index,columns=tick_list)
df2=pd.DataFrame(index=df.index,columns=tick_list)
df3=pd.DataFrame(index=df.index,columns=tick_list)
df4=pd.DataFrame(index=df.index,columns=tick_list)
df5=pd.DataFrame(index=df.index,columns=tick_list)

ii=0
for i in tick_list:
    print i
    sqll2="SELECT adv3.quarterenddate, adv3.workingcapital+ adv3.netfixedassets + adv3.depreciation - adv3.intangibles as ROC,\
    adv3.shorttermdebt+ adv3.longtermdebt+adv3.minorityinterestliability+adv3.preferredstockequity\
    +adv3.cashequivalents as EY,adv3.totalcommonsharesout,adv3.ebit\
    FROM test.adv3\
    where ticker = '%s';" %(i)
    x=sql.read_frame(sqll2, con,'quarterenddate',parse_dates=['quarterenddate'], coerce_float=['totalcommonsharesout'])
    x=x.iloc[0:-1,:]

    
    
    #adjustment to dataframe======
    try:
        x=x.fillna(np.nan)
        x['ebit']=pd.rolling_sum(x['ebit'],4)  
        x['totalcommonsharesout']=x['totalcommonsharesout'].apply(f)
        x['SHARE_V']=dfp[i]*x['totalcommonsharesout'].apply(f)
        x['EY']=x['EY']+x['SHARE_V']
        x['EY']=x['ebit']/x['EY']
        x['ROC']=x['ebit']/x['ROC']
        x['p']=dfp[i]
        x=x[['ROC','EY']]
    except:
        x=pd.DataFrame(index=x.index,columns=['ROC','EY'])

    if ii==0:
        pass
    else:pass
    
    y=pd.DataFrame(x.iloc[:,0].apply(f).values,columns=[i],index=x.index)
    df1=df1.combine_first(y)
    if len(x.columns)>1:
        y=pd.DataFrame(x.iloc[:,1].apply(f).values,columns=[i],index=x.index)
        df2=df2.combine_first(y)
        if len(x.columns)>2:
            y=pd.DataFrame(x.iloc[:,2].apply(f).values,columns=[i],index=x.index)
            df3=df3.combine_first(y)
            if len(x.columns)>3:
                y=pd.DataFrame(x.iloc[:,3].apply(f).values,columns=[i],index=x.index)
                df4=df4.combine_first(y)
                if len(x.columns)>4:
                    y=pd.DataFrame(x.iloc[:,4].apply(f).values,columns=[i],index=x.index)
                    df5=df5.combine_first(y)
                else:pass
            else:pass
        else:pass
    else:pass
    ii +=1
print df3
df1=df1.ffill()
df2=df2.ffill()
df3=df3.ffill()
df4=df4.ffill()
df5=df5.ffill()
# df1.to_excel('C:\Users\oskar\Documents\doc_no_backup\python_crap\excel\sigs.xlsx', 'Sheet1')

   




#signal
sig1=of.replace_na_with_avg(df1)
sig2=of.replace_na_with_avg(df2)
# sig.to_csv("C:\Users\oskar\Documents\doc_no_backup\python_crap\excel\sigb.csv")
rank1=sig1.rank(axis=1) #high is higher rank
rank2=sig2.rank(axis=1) #high is higher rank
# rank.to_csv("C:\Users\oskar\Documents\doc_no_backup\python_crap\excel\df1b.csv")
rank=rank1+rank2
rank=rank.rank(axis=1)
print rank.tail(8)
# rank.to_excel('C:\Users\oskar\Documents\doc_no_backup\python_crap\excel\sigs.xlsx', 'Sheet1')
# rank1.to_excel('C:\Users\oskar\Documents\doc_no_backup\python_crap\excel\sigs.xlsx', 'Sheet2')
# rank2.to_excel('C:\Users\oskar\Documents\doc_no_backup\python_crap\excel\sigs.xlsx', 'Sheet3')

#date lineup------------------------------------------------------------------------------
ss=rank.reindex_like(dfp).ffill()
ss=ss.fillna(0)
ss.to_csv("C:\Users\oskar\Documents\doc_no_backup\python_crap\excel\ssb.csv")




# #return by signal------------------------very slow----------------------------------------------
# sorted_returns = op.rankreturn(ss,ret)
# pnl=(sorted_returns+1).cumprod()
# # print sorted_returns.tail(22)
# # print pnl.tail(22)
# pnl.iloc[-1,:].plot(kind='bar'); plt.axhline(1, color='k')
# # sorted_returns.boxplot()
# plt.show()

#bucket returns--------------------------------------------------------------------------
b=op.ret_buy_bucket(ss,ret,buckets)
pnl=(b+1).cumprod()
pnl.to_csv("C:\Users\oskar\Documents\doc_no_backup\python_crap\excel\pnl_buck.csv")
print pnl.head(3)

fig, axes = plt.subplots(nrows=3, ncols=1)


pnl.iloc[-1,:].plot(kind='bar',ax=axes[0])

# pnl.iloc[-1,:].plot(kind='bar'); plt.axhline(1, color='k')
# pnl.plot(); plt.axhline(1, color='k')
pnll=pnl.applymap(l)
# plt.subplot(212)
pnl.iloc[:,[1,2,3,-3,-2,-1]].plot(ax=axes[1])
plt.legend(loc='best')
pnll.iloc[:,[1,2,3,-3,-2,-1]].plot(ax=axes[2])#; plt.axhline(1, color='k')
plt.legend(loc='best')
plt.show()



 

    
