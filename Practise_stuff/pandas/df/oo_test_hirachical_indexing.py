import numpy as np
randn = np.random.randn
import pandas as pd
from pandas import Series, DataFrame


#print np.arange(4)
val= randn(5,2)
#df=pd.DataFrame(val,columns=['a','b'],index=[[1,1,3,4,4],[1,2,1,1,2]])
df=pd.DataFrame(val,columns=['a','b'])
df['c']=[1,1,3,4,4]
df['d']=[1,2,1,1,2]
print df


#a=df[['c','d']].values
#a=a.T.tolist()
#df2=pd.DataFrame(df[['a','b']].values,columns=['a','b'],index=a)
#df2=pd.DataFrame(df[['a','b']].values,columns=['a','b'],index=df[['c','d']].values.T.tolist())
df2=pd.DataFrame(df['b'].values,index=df[['c','d']].values.T.tolist())
print df2

print df2.unstack(0)
print df2.unstack(1)
