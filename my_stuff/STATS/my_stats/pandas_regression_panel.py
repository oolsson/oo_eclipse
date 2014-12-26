import pandas as pd
import numpy as np
import statsmodels as sm
import statsmodels.api as smf
from pandas.stats.plm import PanelOLS



x1= np.random.randn(20).T
x2=np.random.randn(20).T
x3=np.random.randn(20).T
x4=np.random.randn(20).T
y=0.3*x1+0.3*x2+0.3*x3+0.1*x4
data=np.array([y,x1,x2,x3])
data=np.transpose(data)
df=pd.DataFrame(data,columns=['y','x1','x2','x3'])
# model1 = pd.ols(y=df['y'], x=df[['x1','x2','x3']])
# print df 
# model1 = pd.ols(y=df['y'], x=df['x1'])
# print model1                                                        #test the simple reg model

#setup panel
d={}
list=['A','B','C','D']
for i in range(0,len(list)):
    d[i]=df 
p=pd.Panel.from_dict(d, orient='minor')
p.minor_axis=list
dfy=p['y']
del p['y']
# p['x1']['A']=x4

# print dfy.to_string()
# print '-----------'
print p.items
print p.major_axis
print p.minor_axis
# print p['x3']['D']
print p.ix['x3', :, 'D']   #items, major, minor
p.ix['x3', :, 'D']=12
print p.ix['x3', :, :]

#these are consolidated panel regressions 
model = pd.ols(y=dfy, x=p,entity_effects=True,intercept=False)
print model
model = pd.ols(y=dfy, x=p,intercept=False)                           #compare to simple reg model
print model

#this is splitting a consolidated medel in the individual components
# model = pd.ols(y=dfy, x=p,pool=False,intercept=False)
# print model
# print model.summary_as_matrix['B']
# print model.beta
# for attr in model.ATTRIBUTES:pass
#     print attr
# print help(pd.ols)

