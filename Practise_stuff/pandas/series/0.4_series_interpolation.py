import numpy as np
randn = np.random.randn
import pandas as pd

#NOT WORKING

s3 = pd.Series(['A', 'B', 'C', 'Aaba', 'Baca', '', np.nan, 'CABA', 'dog', 'cat'])
print s3
s3.str.replace('^.a|dog', 'XX-XX ', case=False)
print s3
