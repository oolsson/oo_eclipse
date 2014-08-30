import numpy as np
randn = np.random.randn
import pandas as pd

df = pd.DataFrame({'A' : [1., np.nan, 3., 5., np.nan],
                'B' : [np.nan, 2., 3., np.nan, 6.]})
print df
df=df.reindex(index=['A','B'])
print df
