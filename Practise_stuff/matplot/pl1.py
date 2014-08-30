'''
Created on Feb 18, 2012

@author: oo
'''
import matplotlib.pyplot as plt
import numpy as np


#plt.plot([1,2,3,4], [1,4,9,16])
#plt.show()
#
#plt.plot([1,2,3,4], [1,4,9,16], 'ro')
#plt.axis([0, 6, 0, 20])
#plt.show()


t = np.arange(0., 5., 0.2)
plt.plot(t, t, 'r--', t, t**2, 'bs', t, t**3, 'g^')
plt.show()


o=np.arange(1,2,0.2)
plt.plot(o)
plt.show()

