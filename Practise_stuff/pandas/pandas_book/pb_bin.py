import numpy as np
randn = np.random.randn
import pandas as pd
from pandas import Series, DataFrame

ages = [20, 22, 25, 27, 21, 23, 37, 31, 61, 45, 41, 32]
bins = [18, 25, 35, 60, 100]

cats = pd.cut(ages, bins)
print cats
print cats.labels
print pd.value_counts(cats)


data = np.random.randn(1000) # Normally distributed
cats = pd.qcut(data, 4) # Cut into quartiles
print pd.value_counts(cats)