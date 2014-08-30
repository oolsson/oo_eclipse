# http://scikit-learn.github.io/scikit-learn-tutorial/general_concepts.html#supervised-learning-model-fit-x-y
#2.3
from sklearn.datasets import load_iris
from sklearn.decomposition import PCA
import numpy as np
import pylab as pl
from itertools import cycle
from sklearn.cluster import KMeans
from numpy.random import RandomState

iris = load_iris()
n_samples, n_features = iris.data.shape
#print iris.data
#print iris.target
#print iris.target_names
#print n_samples
#print n_features

#step 1   setup x and y----------------------------------
X, y = iris.data, iris.target

pca = PCA(n_components=2, whiten=True).fit(X)
print pca.components_
print pca.explained_variance_ratio_ 
print pca.explained_variance_ratio_.sum()
X_pca = pca.transform(X) #project the iris dataset along those first 3 dimensions: 2 vectors

#check that dataset has been normalized and have no correlation
print np.round(X_pca.mean(axis=0), decimals=5)
print np.round(X_pca.std(axis=0), decimals=5)
print np.round(np.corrcoef(X_pca.T), decimals=5)

def plot_2D(data, target, target_names):
    colors = cycle('rgbcmykw')
    target_ids = range(len(target_names))
    pl.figure()
    for i, c, label in zip(target_ids, colors, target_names):
        pl.scatter(data[target == i, 0], data[target == i, 1],
                   c=c, label=label)
    pl.legend()
    pl.show()
#plot_2D(X_pca, iris.target, iris.target_names)

rng = RandomState(42)
print rng
kmeans = KMeans(3, random_state=rng).fit(X_pca)
print np.round(kmeans.cluster_centers_, decimals=2)
print kmeans.labels_[:10]
print kmeans.labels_[-10:]
plot_2D(X_pca, kmeans.labels_, ["c0", "c1", "c2"])
