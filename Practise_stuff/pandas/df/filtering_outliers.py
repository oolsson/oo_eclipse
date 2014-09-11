import numpy as np
randn = np.random.randn
import pandas as pd
from pandas import Series, DataFrame

np.random.seed(12345)

data = DataFrame(np.random.randn(1000, 4),columns=['a','b','c','d'])
print data.describe()
# print data.iloc[2:,1:].head(8)

def oo_outlier_filter(data,std_limit):
    std= data.std(0)
    for i in data.columns:
        print std[i]
        data[i][np.abs(data[i]) > std[i]*std_limit] = np.nan       
    return data.fillna(method='ffill')


# # col = data[3]
# # print col[np.abs(col) > 3]
# for i in range(0,len(data.columns)):
#     print i
#     print data.icol[:,1:].describe()
# # print data[(np.abs(data) > 3).any(1)]  #To select all rows having a value exceeding 3 or -3, you can use the any method on a boolean DataFrame:
# # data[np.abs(data) > 3] = np.sign(data) * 3

d=oo_outlier_filter(data,2)
print d.describe()
# print data.head(20)