import random
import matplotlib.pyplot as plt
import numpy as np

nwalks = 100
nsteps = 500
draws = np.random.randint(0, 2, size=(nwalks, nsteps)) # 0 or 1
steps = np.where(draws > 0, 1, -1)
walks = steps.cumsum(1)
walks
print walks
walks=walks.T

plt.plot(walks)
plt.show()