import pandas as pd
import numpy as np
from pandas.io.parsers import *

# index = pd.date_range('1/1/2000', periods=8)
# df = pd.DataFrame(np.ones((8, 3)), index=index,
#                columns=['A', 'B', 'C'])
# df2 = pd.DataFrame(np.random.randint(2, size=(8, 3)), index=index,
#                columns=['A', 'B', 'C'])
xl = pd.ExcelFile("C:/Users/oskar/Documents/doc_no_backup/python_crap/excel/testdata.xls")
ret_individual = xl.parse("Sheet1")
df2 = xl.parse("Sheet2")
rank=df2.rank(axis=1)
# pct_rank=rank/len(rank.columns)

def ret_buy_bucket(rank,ret,num_buckets):
#     print rank
    step=float(1)/float(num_buckets)
    print step
    LI=[step for i in range(0, num_buckets)]
    LI=[0]+LI
    LI=np.cumsum(LI)
    LI=list(LI)
    print LI
    for i in LI:
        print i
        if i==0:pass
        else:
            upper=i
            lower=i-step
            print upper, lower
            pct_rank=rank/len(rank.columns)
            sig=(pct_rank[(pct_rank>lower) & (pct_rank<=upper)])*1
            sig=sig.fillna(0)
            sig=(sig>0)*1
            sig2=sig.sum(axis=1)[-1]
            w_sig = sig/float(sig2)
            w_ret=w_sig*ret
            w_ret = w_ret.sum(axis=1)
            print sig
            print w_ret

    

#     print w_ret

xx=ret_buy_bucket(rank,df2,3)
# ret=sig*ret_individual
# ret2=ret.sum(axis=1)

# print pct_rank
# print ret2
# print rank.groupby(rank.iloc[0])
