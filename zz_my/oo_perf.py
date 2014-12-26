import numpy as np
import pandas as pd
from itertools import repeat
from itertools import chain


def oo_index(df):
    df=df.ffill()
    df=df.pct_change(periods=1)+1
    df=df.cumprod()
#     print df.iloc[1:3.:]
    df.iloc[0,:]=1
    return df


#signal alaysis
def oo_equal_period(df,per):
    df=df.iloc[:,0]
    
    ii=1
    l=[]
    for i in range(0,per):
        f=list(repeat(ii,len(df)/per))
        ii +=1
        l.append(f)
    l=list(chain.from_iterable(l))
    for i in range(0,len(df)%per): l.append(3)
    df=pd.DataFrame(df)
    df['sig']=l
    
    df2=df.iloc[:,0].groupby(df['sig'])
    df3=pd.DataFrame(index=list(range(1,len(df)/per)))
    for i in df2.groups:
        ii=df2.get_group(i).reset_index()
        try:
            df3[i]=ii.iloc[:,1]
        except:print 'something wrong'
    df3=df3.ffill()
    df3=df3.pct_change(periods=1)+1
    df3=df3.cumprod()
#     print df.iloc[1:3.:]
    df3.iloc[0,:]=1
    return df3

def oo_perf_stats(df, annulize=252):
    df=df.ffill()
    df=df.pct_change(periods=1)+1
    df.iloc[0,:]=1
    df_stat=pd.DataFrame(index=['ret_t','ret_a','std','rr','Max_dd','active_r','TE'],columns=df.columns)
    df_stat.loc['ret_t']=df.prod()-1
    af=float(annulize)/len(df.index)
    df_stat.loc['ret_a']=(df_stat.loc['ret_t']+1)**float(af)-1
    df_stat.loc['std']=df.std()*np.sqrt(annulize)
    df_stat.loc['rr']=df_stat.loc['ret_a']/df_stat.loc['std']
    return df_stat

def oo_perf_per_sig(df):
    df2=df.iloc[:,:-1]
    df2=df2.pct_change(periods=1)+1
    df.iloc[:,:-1]=df2.shift(1)
    df2=df.groupby(df['sig_c']).prod()
    df3=df.groupby(df['sig_c']).count()
    af=float(252)/df3
    df3=df2**af
    df3=df3.iloc[:,:-1]
    return df3

def oo_split_bysig(df):
    df.iloc[:,0]=df.iloc[:,0].pct_change(periods=1).shift(1)
    df2=df.iloc[:,0].groupby(df['sig_c'])
    df3=pd.DataFrame()
    for i in df2.groups:
        ii=df2.get_group(i).reset_index()
        if len(ii.index)>len(df3.index):
            df3=df3.reindex(index=ii.index)
        else:pass
        df3[i]=ii.iloc[:,1]
    return df3

def rankreturn(rank,ret):
    """will create returns buy signal strength"""
    rank_sorted=pd.DataFrame(np.ones_like(rank),index=rank.index)-1
    for i in range(0,len(rank.index)):
        for ii in range(0,len(rank.columns)):
            iint=int(rank.iloc[i,ii])
            rank_sorted.iloc[i,int(iint)]=ret.iloc[i,ii]#ret.iloc[i,ii]
    return rank_sorted

def ret_buy_bucket(rank,ret,num_buckets):
    print rank.tail(5)
    rank=rank.fillna(0)
    ret=ret.fillna(0)
    step=float(1)/float(num_buckets)
    LI=[step for i in range(0, num_buckets)]
    LI=[0]+LI
    LI=np.cumsum(LI)
    LI=list(LI)
    LI2=list(range(0,len(LI)-1))
    ii=0
    dfs=pd.DataFrame(index=rank.index,columns=LI2)
    for i in LI:
        if i==0:pass
        else:
            upper=i
            lower=i-step
            pct_rank=rank/len(rank.columns)+0.00001
            sig=(pct_rank[(pct_rank>=lower) & (pct_rank<upper)])*1
#             print lower,upper
#             print pct_rank.tail(8)
#             print sig.tail(8)
            sig=sig.fillna(0)
            sig=(sig>0)*1
            sig2=sig.sum(axis=1)[-1]
            w_sig = sig/float(sig2)
            w_ret=w_sig*ret
#             if ii==1:
#             print sig.tail(8)
#             else:pass
            w_ret = w_ret.sum(axis=1)
            dfs[ii]=w_ret
            ii+=1
    return dfs

    
