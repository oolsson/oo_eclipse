import pandas as pd
import numpy as np
from pandas.io.parsers import *
from sklearn.decomposition import PCA


print help(pd.ExcelFile)
xl = pd.ExcelFile("C:/Users/oskar/Documents/doc_no_backup/python_crap/excel/ass1.xls", index_col=0)
data = xl.parse("Sheet3")
# data.index=
data.index= data['LGA'][0::]
del data['LGA']
print data.head(4)
d2=np.array(data.values)
pca = PCA().fit(d2)

#pca = PCA(n_components=2, whiten=True).fit(X)

print pca.components_        #think this in eig vectors
print pca.explained_variance_ratio_   #think this in eig vectors
print pca.explained_variance_ratio_.sum()   
##corr_volv=df.corr(df.VOLV-B.ST) not working because of name