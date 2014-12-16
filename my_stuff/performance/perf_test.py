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
dfa=op.oo_index(df)                                    #a
# df=op.oo_equal_period(df,4)                            #2
# df=op.oo_perf_stats(df)                                #3

#regime analysis
df['sig']=(df['e']>pd.rolling_mean(df['e'], 3))*1
df['sig2']=(df['b']>pd.rolling_mean(df['b'], 2))*1
df['sig_c']=oof.oo_uneque_sig(df[['sig','sig2']])


# df=op.oo_perf_per_sig(df[['e','b','sig_c']])            #4
df=op.oo_split_bysig(df[['e','sig_c']])                   #5
dfa=(df+1).cumprod()
# print df

# #report
perf_rep=rp.newreport()
perf_rep.addlogo()
perf_rep.pic=rp.pic_num()
 
plt.subplot(111)
plt.plot(dfa.index,dfa)
perf_rep.pic.new()
plt.savefig("C:/Users/oskar/Documents/doc_no_backup/python_crap/temp/%s.png" %(str(perf_rep.pic.num)))
perf_rep.addimage("C:/Users/oskar/Documents/doc_no_backup/python_crap/temp/%s.png"%(str(perf_rep.pic.num)),7,4,'LEFT')
#         plt.show()
plt.close()
 
perf_rep.writereport('perf')
