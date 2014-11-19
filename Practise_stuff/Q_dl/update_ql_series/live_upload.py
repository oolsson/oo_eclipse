#2014/09/10 is the first yahoo data
import Quandl
from pandas.io.data import DataReader
from datetime import datetime
import pandas as pd
import numpy as np
from datetime import datetime
import datetime as dt



print("code: VAL_SPY")
print("name: SPY_Value")
print("----")
print("DATE ,PE, PB, PS, PC")



xl = pd.ExcelFile("C:\Users\oskar\Documents\doc_backup\quandl\CC3.xls")
df = xl.parse("SPY",  index_col=0,  skiprows=2)
df=df.iloc[0:-45,[1,3,4,5]]
     
#  len(df
# print df.tail(45)
for i in range(0,len(df)):
    print df.index[i],',',df.iloc[i,0],',',df.iloc[i,1],',',df.iloc[i,2],',',df.iloc[i,3]