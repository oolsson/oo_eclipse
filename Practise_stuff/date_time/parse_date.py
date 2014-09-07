import datetime as dt
import pandas as pd
from dateutil.parser import parse

# a = "2012-10-09T19:00:55Z"
a ='1999-08'

b = parse(a).date()

print b.weekday()
print b

df=pd.DataFrame([[1,1,1],[2,2,2]], index=['1999-08','1999-09'])
df[4]=['1999-08','1999-09']

f = lambda x: parse(x).date()
g= lambda y: int(y)

df[5]= df[4].map(f)
df.iloc[1:2,1:3]=df.iloc[1:2,1:3].applymap(g)

print df
print type(df[0]['1999-09']),type(df[1]['1999-08']),type(df[2]['1999-09']),type(df[4]['1999-09']),type(df[5]['1999-09'])
print '------------'
print df.iloc[1:2,1:]