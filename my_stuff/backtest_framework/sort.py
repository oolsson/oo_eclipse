import pandas as pd
import numpy as np
from pandas.io.parsers import *

index = pd.date_range('1/1/2000', periods=3)
df = pd.DataFrame([[1,2,3],[2,3,1],[1,3,2]], index=index,
               columns=['C', 'B', 'A'])
rank=df.rank(axis=1)

ret = pd.DataFrame([[0.1,0.2,0.3],[0.2,0.3,0.1],[0.1,0.3,0.2]], index=index,
               columns=['C', 'B', 'A'])


def rankreturn(rank,ret):
    """will create returns buy signal strength"""
    rank_sorted=pd.DataFrame(np.ones_like(rank),index=rank.index)
    for i in range(0,len(rank.columns)):
        for ii in range(0,len(rank.columns)):
            print rank.iloc[i,ii] #first is index second is column
            rank_sorted.iloc[i,int(rank.iloc[i,ii]-1)]=ret.iloc[i,ii]
    return rank_sorted
        
sorted_returns = rankreturn(rank,ret)
pnl=(sorted_returns+1).cumprod()

print rank
print sorted_returns
print pnl

