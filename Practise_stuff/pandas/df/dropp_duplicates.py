import numpy as np
randn = np.random.randn
import pandas as pd



df1 = pd.DataFrame(randn(8,3),columns=['a','b','a'])
# del df1['a']
df1=df1.T.groupby(level=0).first().T
# df1=df1.reindex(columns=['a','b'])
# df1=df1.drop_duplicates()
print df1


df3 = pd.DataFrame([[1,1],[2,1],[1,1],[3,1],[1,1],[5,1]],columns=['a','b'])
df3=df3.drop_duplicates('a')
print df3


#'----combining data'
# print df1
# print df2
#print df1+df2
#print df1.combine_first(df2)

# df=df1.append(df3)
# print df



