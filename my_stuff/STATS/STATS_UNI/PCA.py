import pandas as pd
import numpy as np
from pandas.io.parsers import *
from sklearn.decomposition import PCA

# np.log(2.888)

# print help(pd.ExcelFile)
xl = pd.ExcelFile("C:/Users/oskar/Documents/GitHub/oo_eclipse/my_stuff/Data/ass1.xls", index_col=0)
data = xl.parse("Sheet3")
 
data.index= data['LGA'][0::]
del data['LGA']
print data.head(4)

f = lambda x: np.log(x)
data=data.applymap(f) 

print data.head(4)

d2=np.array(data.values)
pca = PCA().fit(d2)

#pca = PCA(n_components=2, whiten=True).fit(X)

# print pca.components_        #think this in eig vectors
# print pca.explained_variance_ratio_   #think this in eig vectors
# print pca.explained_variance_ratio_.sum()   
##corr_volv=df.corr(df.VOLV-B.ST) not working because of name