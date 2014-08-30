import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

i1 = pd.date_range('2012-06-01', '2012-07-03')
i2 = pd.date_range('2012-06-01', '2012-09-01',freq='W')

df1=pd.Series(np.ones(len(i1)),index=i1)
df1=pd.DataFrame(df1,columns=['A'])
df2=pd.DataFrame(np.random.randn(len(i2)),index=i2,columns=['B'])
#df2=df2.asfreq('W', method='pad')

print df1
print df1['A'][1].astype(str)
print df2

port=df1.combine_first(df2).fillna(method='ffill').astype(str)
port['C']=port['A']+port['B']

print port



#combine method 1
#port= pd.merge(df1, df2, how='outer', left_index=True, right_index=True)
#port=port.asfreq('D', method='pad')
#port['conc']=pd.concat(port['A'],port['B'])
#print port