from sklearn.datasets import load_iris
from sklearn.linear_model import LogisticRegression

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
clf  = LogisticRegression()
#step 3 fit data-------------------------------------------
clf = clf.fit(X, y)
#print clf.coef_
#print clf.intercept

# Step 4  predict-------------------------------------------------------
X_new = [[ 5.0,  3.6,  1.3,  0.25]]
print clf.predict(X_new) #'predict the most likely outcome'
print clf.predict_proba(X_new) #'probabileties of the different outcomes'