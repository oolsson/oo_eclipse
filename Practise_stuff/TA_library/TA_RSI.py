import numpy
import talib
from pandas.io.data import DataReader
from datetime import datetime
import pandas as pd
import matplotlib.pyplot as plt


f = lambda x: float(x)
SPX = DataReader("SP500",  "fred", datetime(2011,1,1), datetime(2012,1,11)).applymap(f).bfill() #SPX
SPX['ma']=talib.SMA(SPX['SP500'],5)
SPX['mom']=talib.MOM(SPX['SP500'], timeperiod=5)
SPX['RSI']=talib.RSI(SPX['SP500'], timeperiod=14)
print SPX.tail(7)

plt.show(plt.plot(SPX))
