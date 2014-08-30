'''
Created on Feb 18, 2012

@author: oo
'''
import numpy as np
import matplotlib.pyplot as plt

def f(t):
    return np.exp(-t) * np.cos(2*np.pi*t)

t1 = np.arange(0.0, 5.0, 0.1)
t2 = np.arange(0.0, 5.0, 0.02)

plt.figure(1)
plt.subplot(211)
plt.plot(t1, f(t1), 'bo', t2, f(t2), 'k')

plt.subplot(212)
plt.plot(t2, np.cos(2*np.pi*t2), 'r--')
plt.show()

'---------------------------------------'

o1=np.arange(1,10,1)
o2=np.arange(10,1,-1)
o3=np.arange(1,22,1)


plt.figure(1)
plt.subplot(311)
plt.plot(o1, 'r')
plt.subplot(312)
plt.plot(o2, 'b')
plt.subplot(313)
plt.plot(o3, 'g')


plt.show()