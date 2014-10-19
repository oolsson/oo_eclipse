import numpy as np
randn = np.random.randn
import pandas as pd

dates = np.asarray(pd.date_range('1/1/2000', periods=8))
df = pd.DataFrame(randn(8, 4), index=dates, columns=['A', 'B', 'C', 'D'])
dates = np.asarray(pd.date_range('1/1/2000', periods=12))
df2 = pd.DataFrame(randn(12, 4), index=dates, columns=['A', 'B', 'C', 'D'])

# print df
# df=pd.rolling_max(df, 4,True)
# print df

print df
print df2
df3=df+df2
print df3