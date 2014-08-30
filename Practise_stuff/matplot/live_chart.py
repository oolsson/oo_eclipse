'''
Created on Feb 26, 2012

@author: oo
'''
import matplotlib.pyplot as plt
import numpy as np
import time

number=[1]
x=0
plt.plot([number])
plt.show()

while x<8:
    x +=1
    number.append(x)
    time.sleep(1)
    plt.plot([number])
        
print number
