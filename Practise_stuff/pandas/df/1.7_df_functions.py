import numpy as np
randn = np.random.randn
import pandas as pd



index = range(12)
df = pd.DataFrame(randn(12, 3), index=index,
                  columns=['A', 'B', 'C'])

print df                                                 #print df
#print df.apply(np.mean)                                 #print mean long columns
#print df.apply(np.mean, axis = 1)                       #print mean along rows
#print df.apply( lambda x: x.max() - x.min())            #print diff max min along columns
#print df.apply(np.cumsum)                                #print cumsum long columns
#print df.apply(lambda x: x.index[x.dropna().argmax()])   #finds the index value of the max of each colums

'''
print 'custom function where you pass arguments
def subtract_and_divide(x, sub, divide=1):
    return (x - sub) / divide

df.apply(subtract_and_divide, args=(5,), divide=3)
'''

'''
print 'apply a function to one col or many entire data frame'
f = lambda x: x+100
print df['A'].map(f)
print df.applymap(f)
'''
