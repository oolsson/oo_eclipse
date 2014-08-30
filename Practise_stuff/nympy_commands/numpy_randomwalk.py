import random
import matplotlib.pyplot as plt
import numpy as np

position = 0
walk = [position]
steps = 100
for i in xrange(steps):
    step = 1 if random.randint(0, 1) else -1
    position += step
    walk.append(position)
print walk

#or
nsteps = 100
draws = np.random.randint(0, 2, size=nsteps)
steps = np.where(draws > 0, 1, -1)
walk2 = steps.cumsum()

print walk2
#print walk+walk2
print (np.abs(walk) >= 10).argmax()
print (np.abs(walk2) >= 10).argmax()
#
plt.plot(walk)
plt.show()
plt.plot(walk2)
plt.show()
show()