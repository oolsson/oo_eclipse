from pandas.io.data import DataReader
from datetime import datetime
import pandas as pd
import numpy as np



df = DataReader("GOOG",  "yahoo", datetime(2009,1,1), datetime(2013,5,5))
df=df['Open']
df=df.groupby(df.index.map(lambda x: x.year)).mean()


print df.describe()
print df.to_string