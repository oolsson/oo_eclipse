import pandas as bp
import numpy as np

def oo_outlier_filter(data,std_limit):
    std= data.std(0)
    for i in data.columns:
        print std[i]
        data[i][np.abs(data[i]) > std[i]*std_limit] = np.nan       
    return data.fillna(method='ffill')

def oo_uneque_sig(df):
    portsig_str=df.astype(str)
    df['sig_c']=portsig_str.iloc[:,0]
    for i in range(2,len(df.columns)):
        print i
        df['sig_c']=df['sig_c']+portsig_str.iloc[:,i-1]
#     df['sig_c']=portsig_str['sig']+portsig_str['sig2']
    return df['sig_c']