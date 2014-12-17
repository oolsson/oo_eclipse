from pandas.io.data import DataReader
from datetime import datetime
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import zz_my.reportclss as rp
import zz_my.oo_functions as oof
import zz_my.oo_perf as op
import Quandl

xl = pd.ExcelFile("C:\Users\oskar\Documents\GitHub\oo_eclipse\my_stuff\Data\sp500.xls")
df = xl.parse("sheet1",  index_col=0,  skiprows=0)
# print df.head(3)
 

df.columns=['e','b']
df1=op.oo_index(df)                                      #1
df2=op.oo_equal_period(df,4)                            #2
df3=op.oo_perf_stats(df)                                #3

#regime analysis
df['sig']=(df['e']>pd.rolling_mean(df['e'], 3))*1
df['sig2']=(df['b']>pd.rolling_mean(df['b'], 2))*1
df['sig_c']=oof.oo_uneque_sig(df[['sig','sig2']])


df4=op.oo_perf_per_sig(df[['e','b','sig_c']])            #4
df5=op.oo_split_bysig(df[['e','sig_c']])                   #5
df5=(df5+1).cumprod()
# print df

# #report
perf_rep=rp.newreport()
perf_rep.addlogo()
perf_rep.pic=rp.pic_num()
#  

perf_rep.add_plot(df1,title1='ll')
perf_rep.add_df(df3, 1, 1)
perf_rep.add_plot(df2,title1='ll')

# perf_rep.add_plot(df3,title1='ll')
# perf_rep.add_plot(df4,title1='ll')
perf_rep.add_plot(df5,title1='ll')
perf_rep.add_df(df4, 1, 1)
# perf_rep.add_df(df, 1, 1)
 
perf_rep.writereport('perf')
