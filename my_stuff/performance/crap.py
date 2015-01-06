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
sqll="SELECT ticker FROM test.index_constit where indexx = 'SP500' and ticker like 'w%';"
# sqll="SELECT ticker FROM test.index_constit where indexx = 'SP500';"
tick_list=sql.read_frame(sqll, con)
tick_list=list(tick_list['ticker'])
print tick_list

con = mdb.connect('localhost', "root","","test");
# sqll2="SELECT freecashflow,EBIT,quarterenddate,grossmargin FROM test.adv3 where ticker = 'YHOO';"
# roe=sql.read_frame(sqll2, con,'quarterenddate',parse_dates=['quarterenddate'])



#sig data-----------------------------------------------------------------------------
df=pd.DataFrame()
df1=pd.DataFrame(index=df.index,columns=tick_list)
df2=pd.DataFrame(index=df.index,columns=tick_list)
df3=pd.DataFrame(index=df.index,columns=tick_list)
df4=pd.DataFrame(index=df.index,columns=tick_list)
df5=pd.DataFrame(index=df.index,columns=tick_list)


for i in tick_list:
    sqll2="SELECT quarterenddate,freecashflow,EBIT,grossmargin FROM test.adv3 where ticker = '%s';" %(i)
    x=sql.read_frame(sqll2, con,'quarterenddate',parse_dates=['quarterenddate'])
    x=x.iloc[0:-1,:]
    
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
    
print df1
