import random
import pandas as pd
import numpy as np
import time
import heapq

df=pd.DataFrame(np.random.uniform(0,1,11))
x=heapq.nlargest(2, df.values)

df2=pd.DataFrame(index=df.index)
 
for i in range(0,5):
    df=pd.DataFrame(np.random.uniform(0,1,11))
    x=heapq.nlargest(2, df.values)
    df2[i]=(df>=x[1])*1
# df['e']=(df>=x[1])*1
 
print x[0]
print df2

