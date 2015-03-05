import random

class RandomGen():
    def __init__(self):
        # Values that may be returned by next_num()
        self._random_nums = [-1, 0, 1, 2, 3]
        # Probability of the occurence of random_nums
        self._probabilities = [0.01, 0.3, 0.58, 0.1, 0.01]
    
    def next_num(self):
        """
        Returns one of the randomNums. When this method is called
        multiple times over a long period, it should return the
        numbers roughly with the initialized probabilities.
        """
        z=random.random()
        c=0.0
        pos=0
        for i in self._probabilities:
            c+=i
            if z<c:
                num=self._random_nums[pos]
                break
            pos+=1
        return num

rm=RandomGen()
rm.next_num()

#verify
L=[]
for i in range(0,10000):
    L.append(rm.next_num())

print -1,L.count(-1)
print 0, L.count(0)
print 1, L.count(1)
print 2, L.count(2)
print 3, L.count(3)

