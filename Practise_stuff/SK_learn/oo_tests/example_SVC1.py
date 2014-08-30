from sklearn.datasets import load_iris
from sklearn.svm import LinearSVC

iris = load_iris()
n_samples, n_features = iris.data.shape
#print iris.data
#print iris.target
#print iris.target_names
#print n_samples
#print n_features

#step 1   setup x and y----------------------------------
X, y = iris.data, iris.target
#step 2   choose algorithom----------------------------------------
clf = LinearSVC()
#step 3 fit data-------------------------------------------
clf = clf.fit(X, y)
#print clf.coef_
#print clf.intercept

# Step 4  predict-------------------------------------------------------
X_new = [[ 5.0,  3.6,  1.3,  0.25]]
print clf.predict(X_new)