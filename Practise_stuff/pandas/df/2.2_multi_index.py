import numpy as np
randn = np.random.randn
import pandas as pd

dates = np.asarray(pd.date_range('1/1/2000', periods=8))
df = pd.DataFrame(randn(8, 4), index=dates, columns=['A', 'B', 'C', 'D'])

print df

subindex = dates[[3,4,5]]
print df.ix[subindex, ['C', 'B']]

df2 = df.copy()
df2.ix[subindex, ['C', 'B']] = 0
print df2

print 'slicing-------------'
print df.ix[1:7, :2]

print 'select -------------'
print df.select(lambda x: x == 'A', axis=1)

print 'multi index'
arrays = [np.array(['bar', 'bar', 'baz', 'baz', 'foo', 'foo', 'qux', 'qux']),
          np.array(['one', 'two', 'one', 'two', 'one', 'two', 'one', 'two'])]

df = pd.DataFrame(randn(8, 4), index=arrays, columns=['A', 'B', 'C', 'D'])
print df
# can be found more of here In [685]
df2 = df.mean(level=1)
print df2

print 'resetting indexes'
df=df.reset_index()
print df
df.columns=['A', 'B', 'C', 'D','E','F']
print df
df=df.set_index(['A', 'B'])
print df

