'''
Created on Feb 5, 2013

@author: oo
'''
import pandas as pd
import numpy as np

df1 = pd.DataFrame(np.arange(12.).reshape((3, 4)), columns=list('abcf'),index=['o','s','k'])
#print df1
df2 = pd.DataFrame(np.arange(20.).reshape((4, 5)), columns=list('abcde'),index=['o','s','a','r'])
df3=df1.add(df2, fill_value=0)
df4=df1.add(df1, fill_value=0)
#print df3
#print df4
index= df2.index+df1.index
col=df2.columns+df1.columns
#print index
df5=df1.reindex(index, columns=col).fillna(0)
#print df5
df6=df2.reindex(index, columns=col).fillna(0)
#print df6
df7=df5+df6
#print df7
odf=df7['f']
print odf

df7['s2']=df7['f']
print df7

df7['send']=df7['f']
i=1
while i < len(df7['f']):
    if (df7['f'].ix[i]>2):
        df7['send'].ix[i]=1
        print df7.index[i]
        print df7['s2'].ix[i]
          
    else:
        df7['send'].ix[i]=0
    i=i+1
print df7
df7[('s2','f')]=0
print df7






