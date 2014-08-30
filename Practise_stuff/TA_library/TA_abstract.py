import numpy as np
import talib
from pandas.io.data import DataReader
from datetime import datetime
import pandas as pd
import matplotlib.pyplot as plt


f = lambda x: float(x)
SPX = DataReader("SP500",  "fred", datetime(2011,1,1), datetime(2012,1,11)).applymap(f).bfill() #SPX
# SPX['ma']=SPX['SP500'].apply(abstract.Function('sma'))

SPX['SMA'] = talib.MA(SPX.SP500, 15)
print SPX.to_string()

print talib.get_functions()
#https://github.com/mrjbq7/ta-lib