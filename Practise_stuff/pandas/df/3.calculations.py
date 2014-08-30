import numpy as np
randn = np.random.randn
import pandas as pd

dates = np.asarray(pd.date_range('1/1/2000', periods=8))
df = pd.DataFrame(randn(8, 4), index=dates, columns=['A', 'B', 'C', 'D'])

print df
#print df.rank(1)

df2=pd.rolling_corr(df, df['B'], window=5)
print df2

correls = pd.rolling_corr_pairwise(df, 5)
print correls[df.index[1]]
print correls[df.index[6]]
correls.ix[:, 'A', 'C'].plot()  #Not working