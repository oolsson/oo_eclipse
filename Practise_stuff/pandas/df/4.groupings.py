import numpy as np
randn = np.random.randn
import pandas as pd

df = pd.DataFrame({'A' : ['foo', 'bar', 'foo', 'bar',
                       'foo', 'bar', 'foo', 'foo'],
                'B' : ['one', 'one', 'two', 'three',
                       'two', 'two', 'one', 'three'],
                'C' : randn(8), 'D' : randn(8)})
print df
print '--------------------'
grouped = df.groupby('A').groups
print grouped
print '--------------------'
df2 = pd.DataFrame({'X' : ['B', 'A', 'A', 'A'], 'Y' : [1, 2, 3, 4]})
print df2
print '--------------------'
print df2.groupby(['X'], sort=True).sum()
