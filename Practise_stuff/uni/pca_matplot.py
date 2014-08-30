from matplotlib.mlab import PCA
import numpy as np
data = np.array(np.random.randint(10,size=(10,3)))
results = PCA(data)
print help(results)
print results.Wt
print results.Y
