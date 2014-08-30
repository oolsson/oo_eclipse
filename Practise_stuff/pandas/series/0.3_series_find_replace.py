import numpy as np
randn = np.random.randn
import pandas as pd

print 'NOT WORKING YET'

s = pd.Series(randn(7), index=['a','b','c','d','e','f','g'])
d = {'a' : 0., 'b' : 1., 'e' : 2., 'f' : 1., 'g' : 2.}
oo=pd.Series(d)

#print oo
#print oo + s
oo=oo+s
oo.interpolate
print oo



