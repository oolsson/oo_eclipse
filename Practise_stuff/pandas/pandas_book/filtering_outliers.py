import numpy as np
randn = np.random.randn
import pandas as pd
from pandas import Series, DataFrame

np.random.seed(12345)

data = DataFrame(np.random.randn(1000, 4))
print data.describe()

col = data[3]
print col[np.abs(col) > 3]
print data[(np.abs(data) > 3).any(1)]  #To select all rows having a value exceeding 3 or -3, you can use the any method on a boolean DataFrame:
data[np.abs(data) > 3] = np.sign(data) * 3
print data.describe()