import numpy as np
randn = np.random.randn
import pandas as pd

df = pd.DataFrame({'A' : ['foo', 'bar', 'foo', 'bar',
                       'foo', 'bar', 'foo', 'foo'],
                'B' : ['one', 'one', 'two', 'three',
                       'two', 'two', 'one', 'three'],
                'C' : randn(8), 'D' : randn(8)})
print df
df=df.reindex(columns=['A','C'])
print df
print df.columns