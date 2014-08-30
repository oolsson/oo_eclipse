import numpy as np
import math
import random
from scipy import stats
from scipy.stats import norm


class BS():
    def __init__(self,type,spot=100,strike=100,vol=0.2,time=1,i_rate=0.05,div=0):
        self.type=type
        self.spot=float(spot)
        self.strike=float(strike)
        self.vol=float(vol)
        self.time=float(time)
        self.i_rate=float(i_rate)
        self.div=float(div)
        
        self.d1=(math.log(self.spot/self.strike)
                 +(self.i_rate-self.div+(self.vol**2)/2)*self.time)/(self.vol*math.sqrt(self.time))
        self.d2=self.d1-self.vol*math.sqrt(self.time)
        self.Nd1=norm.cdf(self.d1)
        self.Nd2=norm.cdf(self.d2)

    def Price(self):
        if self.type=='call':
            price=self.spot*math.exp(-self.div*self.time)*self.Nd1-self.strike*math.exp(-self.i_rate*self.time)*self.Nd2
        elif self.type=='put':
            price=self.strike*math.exp(-self.i_rate*self.time)*(1-self.Nd2)-self.spot*math.exp(-self.div*self.time)*(1-self.Nd1)
        return price
         
        
#obj=BS('call')
#print obj.Price()

