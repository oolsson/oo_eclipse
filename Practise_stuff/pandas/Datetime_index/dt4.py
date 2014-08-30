from pandas.io.data import DataReader
from datetime import datetime
import datetime as dt
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

LI = pd.date_range('2011-06-01', '2012-06-01', freq='WOM-2FRI')


x=0
for i in LI:
    #rng = pd.date_range(i, periods=5, freq='H')
    rng = pd.date_range(i+dt.timedelta(hours=5), i+dt.timedelta(hours=8), freq='H')
    print i
    if x==0:rng2=rng
    else: rng2=rng2.append(rng)
    x +=1
        

    #print S.index[1]
S=pd.Series(np.ones(len(rng2)),index=rng2)
print S