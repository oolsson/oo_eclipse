import numpy as np
import pandas as pd

ev1=np.array([[1,2,3,4]])
ev2=np.array([[1,2,3,4],[1,2,3,4]])

b=np.array([[1,2,3,4]])
m=np.repeat(b, 5, axis=0)
print m
print ev1
print ev1.T

score = np.dot(m,ev2.T)
print score

dfm=pd.DataFrame(m)
dfev=pd.DataFrame(ev2.T)


print dfm
print '--------'
print dfev

print dfm.shape, ev2.T.shape
pc=dfm.dot(ev2.T)
print pc