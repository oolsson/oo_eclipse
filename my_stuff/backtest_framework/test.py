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
from dateutil import parser
import time
import datetime
import matplotlib.pyplot as plt


f = lambda x: float(x)

# get universe
con = mdb.connect('localhost', "root","","test");
sqll="SELECT ticker FROM test.index_constit where indexx = 'SP500' and ticker like 'c%';"
# sqll="SELECT ticker FROM test.index_constit where indexx = 'SP500';"
tick_list=sql.read_frame(sqll, con)
tick_list=list(tick_list['ticker'])
print tick_list

con = mdb.connect('localhost', "root","","test");
sqll2="SELECT freecashflow,EBIT,quarterenddate,grossmargin FROM test.adv3 where ticker = 'YHOO';"
roe=sql.read_frame(sqll2, con,'quarterenddate',parse_dates=['quarterenddate'])



df1=pd.DataFrame(index=roe.index,columns=tick_list)
df2=pd.DataFrame(index=roe.index,columns=tick_list)
df3=pd.DataFrame(index=roe.index,columns=tick_list)
df4=pd.DataFrame(index=roe.index,columns=tick_list)
df5=pd.DataFrame(index=roe.index,columns=tick_list)

#sig data
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


# df3['av']=df3.mean(axis=1)
df3=df3.T.fillna(df3.T.mean())
df3=df3.T
print df3.to_string()
