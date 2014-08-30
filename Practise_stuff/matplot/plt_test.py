'''
Created on Feb 19, 2012

@author: oo
'''
import matplotlib.pyplot as plt
import numpy as np

y1=[1,2,3,4,4,9,16]

plt.plot(y1)
lines = plt.plot(y1)
plt.setp(lines, color='r', linewidth=2.0)
#plt.show()
plt.setp(y1)


