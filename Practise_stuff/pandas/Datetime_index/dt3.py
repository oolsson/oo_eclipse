from pandas.io.data import DataReader
import datetime as dt
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
randn = np.random.randn

#p = pd.Period('2012Q4', freq='Q-JAN')
p = pd.Period('2012Q4', freq='Q-JAN')
p4pm = (p.asfreq('B', 'e') - 1).asfreq('T', 's') + 16 * 60
#print p4pm

dr = pd.date_range('2009,1,1', '2010,12,31',freq='H')
dt = pd.Series(np.arange(len(dr)),index=dr)
#print dt
#hour = dt.index.hour
#selector = ((10 <= hour) & (hour <= 13)) | ((20<=hour) & (hour<=23))
#data = dt[selector]

#sel = dt.index
LI = pd.date_range('2012-06-01 09:30', '2013-06-01 11:59', freq='WOM-2FRI')
dt = pd.Series(np.arange(len(LI)),index=LI)
SI = pd.date_range('2012-06-01 09:30', '2013-06-01 11:59',freq='H')
dtt = pd.Series(np.arange(len(SI)),index=SI)

#print LI.reindex(freq='H')

#print dt.index[1].date()
#print dt.index.hour==any(dtt.index.hour)
##self.df2=self.df2[self.df2.index.minute==self.df2.index.minute[-1]]



