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

# get universe
con = mdb.connect('localhost', "root","","test");
sqll="SELECT ticker FROM test.index_constit where indexx = 'SP500' and ticker like 'b%';"
# sqll="SELECT ticker FROM test.index_constit where indexx = 'SP500';"
tick_list=sql.read_frame(sqll, con)
tick_list=list(tick_list['ticker'])
print tick_list

con = mdb.connect('localhost', "root","","test");
sqll2="SELECT freecashflow,EBIT,quarterenddate,grossmargin FROM test.adv3 where ticker = 'YHOO';"
roe=sql.read_frame(sqll2, con,'quarterenddate',parse_dates=['quarterenddate'])


#sig data-----------------------------------------------------------------------------
df1=pd.DataFrame(index=roe.index,columns=tick_list)
df2=pd.DataFrame(index=roe.index,columns=tick_list)
df3=pd.DataFrame(index=roe.index,columns=tick_list)
df4=pd.DataFrame(index=roe.index,columns=tick_list)
df5=pd.DataFrame(index=roe.index,columns=tick_list)

for i in tick_list:
    sqll2="SELECT quarterenddate,freecashflow,EBIT,grossmargin FROM test.adv3 where ticker = '%s';" %(i)
    x=sql.read_frame(sqll2, con,'quarterenddate',parse_dates=['quarterenddate'])
    x=x.iloc[0:-1,:]
    df1[i]=x.iloc[:,0].apply(f)
    if len(x.columns)>1:
        df2[i]=x.iloc[:,1].apply(f)
        if len(x.columns)>2:
            df3[i]=x.iloc[:,2].apply(f)
            if len(x.columns)>3:
                df4[i]=x.iloc[:,3].apply(f)
                if len(x.columns)>4:
                    df5[i]=x.iloc[:,4].apply(f)
                else:pass
            else:pass
        else:pass
    else:pass
    print i


    

#price data-----------------------------------------------------------------------------------------
ii=0
for i in tick_list:
    sqll2="SELECT Adj_Close,date FROM test.yahoo_p where ticker = '%s' and date >'2004';" %(i)
    x=sql.read_frame(sqll2, con,'date',parse_dates=['date'])
    if ii==0:
        dfp=x
        dfp.columns=[i]
    else:
        dfp[i]=x['Adj_Close']
    ii +=1
ret=dfp.applymap(f).pct_change(1)

#signal
df3=of.replace_na_with_avg(df3)
rank=df3.rank(axis=1)

#date lineup------------------------------------------------------------------------------
ss=rank.reindex_like(dfp).ffill()
ss=ss.fillna(0)




# #return by signal------------------------very slow----------------------------------------------
# sorted_returns = op.rankreturn(ss,ret)
# pnl=(sorted_returns+1).cumprod()
# # print sorted_returns.tail(22)
# # print pnl.tail(22)
# pnl.iloc[-1,:].plot(kind='bar'); plt.axhline(1, color='k')
# # sorted_returns.boxplot()
# plt.show()

#bucket returns--------------------------------------------------------------------------
b=op.ret_buy_bucket(ss,ret,49)
pnl=(b+1).cumprod()
pnl.iloc[-1,:].plot(kind='bar'); plt.axhline(1, color='k')
plt.show()



 

    
