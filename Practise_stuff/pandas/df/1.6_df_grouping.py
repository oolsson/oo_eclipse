import numpy as np
randn = np.random.randn
import pandas as pd



print 'generating 100  random numbers between 0 and 7 and counting numberes in ofeanch.'
data = np.random.randint(0, 7, size=100)
print 'count values'
print pd.value_counts(data)
s = pd.Series(data)
print s.value_counts() #same as value_counts(data)



print 'generating 100  random numbers between 0 and 7 and counting numberes in of each'
data = np.random.randint(0, 7, size=100)
factor = pd.cut(data, 6)
print pd.value_counts(factor)
print '------------------'



print 'generating 100 normal random numbers and using the percentile count to get count in each percentile.'
data = np.random.randn(100)
factor = pd.qcut(data, [0, 0.01, 0.05, 1])
print pd.value_counts(factor)

