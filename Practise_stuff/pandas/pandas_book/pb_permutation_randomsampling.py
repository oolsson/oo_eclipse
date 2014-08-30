import numpy as np
randn = np.random.randn
import pandas as pd
from pandas import Series, DataFrame

df = DataFrame(np.arange(5*4).reshape((10, 2)))
print df

sampler = np.random.permutation(10)
print sampler

print '-----------'
print df.take(sampler)






