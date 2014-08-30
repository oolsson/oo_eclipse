from sklearn import datasets
import matplotlib.pyplot as plt
import numpy as np
from sklearn.svm import LinearSVC

#a=np.random.binomial(1,0.5,(2,10))
#a=a.T
a=np.array([[1,1,2],
            [1,1,2],
            [0,0,2],
            [0,0,2],
            [0,1,2],
            [0,1,2],
            [1,0,2],
            [1,0,2]])
b=np.array([['dog'],
            ['dog'],
            ['ff'],
            ['ff'],
            ['wof'],
            ['wof'],
            ['cat'],
            ['cat']])

clf = LinearSVC()
X, y = a, b
clf = clf.fit(X, y)
# X_new = [[1,0],  [0,3]]
X_new = [-3,1,2]
print clf.predict(X_new)
print clf.coef_
print clf.intercept_

# print help(clf)
