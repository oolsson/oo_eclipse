import numpy as np
randn = np.random.randn
import pandas as pd

df2 = pd.DataFrame({'a' : ['one', 'one', 'two', 'three', 'two', 'one', 'six'],
                  'b' : ['x', 'y', 'y', 'x', 'y', 'x', 'x'],
                  'c' : randn(7)})

print df2
print df2[df2['a'].isin(['one', 'two'])] #prints the rows where col a has a value of 'onr' or 'two'
print df2[df2['a'] == 'one'] #prints all the rows where column A meets criteria


criterion = df2['a'].map(lambda x: x.startswith('t')) #sets the criteria toitem in col a that starts with t
print df2[criterion]

# Multiple criteria
print df2[criterion & (df2['b'] == 'x')]

#bloean indexing 
print '-----------------------------------------'
df2[df2['c'] < 0] = 0
print df2