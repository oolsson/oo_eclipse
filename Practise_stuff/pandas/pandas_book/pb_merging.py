import numpy as np
randn = np.random.randn
import pandas as pd
from pandas import Series, DataFrame

df1 = DataFrame({'key': ['b', 'b', 'a', 'c', 'a', 'a', 'b'], 'data1': range(7)})
df2 = DataFrame({'key': ['a', 'b', 'd'], 'data2': range(3)})

print pd.merge(df1, df2)
print pd.merge(df1, df2, on='key') #same as previous

df3 = DataFrame({'lkey': ['b', 'b', 'a', 'c', 'a', 'a', 'b'],'data1': range(7)})
df4 = DataFrame({'rkey': ['a', 'b', 'd'], 'data2': range(3)})

print pd.merge(df3, df4, left_on='lkey', right_on='rkey')

print pd.merge(df1, df2, how='outer') #merge defaults to inner, which is only giving values where both dataframes has values 


#  for merging on many keys read page 193