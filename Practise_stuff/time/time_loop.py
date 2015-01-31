
import time

def procedure():
    for i in range(0,20):
        print i
        time.sleep(2)

# measure process time
t0 = time.clock()
procedure()
print time.clock() - t0, "seconds process time"

# measure wall time
t0 = time.time()
procedure()
print time.time() - t0, "seconds wall time"