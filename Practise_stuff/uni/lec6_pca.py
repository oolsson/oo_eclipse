import pandas as pd
from sklearn.decomposition import PCA
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt

#print help(pd.read_csv)

data = pd.read_csv("E:\web\New folder\d_swap.csv",names=['a','b','c','d','f','g','h','i'],dtype=float)
ret=data.pct_change(1).dropna()
#print help(ret.corr)
#print ret.corr(method='pearson')

#sklearn
#pca = PCA().fit(ret.values)
#print pca.components_        #think this in eig vectors
#print pca.explained_variance_ratio_   #eigen values
#print pca.explained_variance_ratio_.sum() 

print '-----------------'
[eval,evec] = np.linalg.eig(ret.corr().values)
print eval #eigen values
print evec #eigenvectors
df_evec=pd.DataFrame(evec)
print df_evec[[0,1,2,3]]
print help(plt.bar)
df_evec[[0,1,2]].plot(kind='bar')
plt.show()
