import numpy as np
randn = np.random.randn
import pandas as pd

#http://pandas.pydata.org/pandas-docs/stable/indexing.html

dates = np.asarray(pd.date_range('1/1/2000', periods=8))
df = pd.DataFrame(randn(8, 4), index=dates, columns=['A', 'B', 'C', 'D'])

'''
#slicing int smaller df and then individula data point
print df
s = df['A']
print s
print s[dates[5]]
print s.get_value(dates[5])           #same but faster
print df.get_value(dates[5], 'A')     #same but faster
print df.set_value(dates[5], 'E', 7)  #seting a value in a new col
df[['B', 'A']] = df[['A', 'B']] #switching columns around
print df
'''

#Accessing rows
# date = dates[5]                     #seting date to a specific index value
# print df.xs(date)                   #accessing the row of the specific index value
# print df[::-1]                      #reversing the index order
# print df[::2]                         #print all columns and every second row

# df2=df.copy()
# df2[:5]=0                       #first 5 rows =0
# print df2

# print df.iloc[1:5,2:4]             #select sub matrix
# df.iloc[1:5,2:4]=0                #setting submatrix to 0
# df.iloc[[0,2,3,4],[0,2,3]]=0     #setting specific cordinates to 0
print df
print df.iat[-1, 0]                  #specific values

# print df
# print df >0
# df2= df[df >0]
# print df2
# df2=df.iloc[[-1]][df.iloc[[-1]]>0].dropna(1).transpose()
# print df2





