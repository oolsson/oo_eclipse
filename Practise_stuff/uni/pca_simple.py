import pandas.io.sql as sql
import MySQLdb as mdb
import pandas as pd
from pandas.tseries.offsets import Hour, Minute
import numpy as np
randn = np.random.randn
from pandas import *
import datetime as dt
import statsmodels as sm
from pandas.io.data import DataReader
from scipy import stats
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA

cc=np.array([[0.1,-0.1,0.1],[-0.1,0.2,-0.1],[0.1,-0.1,0.5]])
#
#corr=df.corr()
#cov=df.cov()
#
#X, y = df.values, df.index
print help(PCA)
#pca = PCA( whiten=True).fit(cc)
pca = PCA().fit(cc)
#pca = PCA(n_components=2, whiten=True).fit(X)

print pca.components_        #think this in eig vectors
print pca.explained_variance_ratio_   #think this in eig vectors
print pca.explained_variance_ratio_.sum()   
##corr_volv=df.corr(df.VOLV-B.ST) not working because of name
