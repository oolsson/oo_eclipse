from pandas.io.data import DataReader
from datetime import datetime
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import zz_my.reportclss as rp
import talib

security=["^GSPC"]
LI = pd.date_range('2011-03-01', '2013-10-01', freq='D')
df=pd.DataFrame(index=LI)

for i in security:
    dfi = DataReader(i,  "yahoo", datetime(2012,6,1), datetime(2013,6,1))
    dfi['ATR'] = talib.ATR(dfi['High'],dfi['Low'],dfi['Close'],10)
    dfi['rMAX20']=pd.rolling_max(dfi['High'],20).shift(1)
    dfi['rMAX8']=pd.rolling_max(dfi['High'],8).shift(1)
    dfi['rMIN20']=pd.rolling_min(dfi['Low'],20).shift(1)
    dfi['rMIN8']=pd.rolling_min(dfi['Low'],8).shift(1)
    dfi['BOH']=(dfi['High']>dfi['rMAX20'])*1
    dfi['BOL']=(dfi['Low']<dfi['rMIN20'])*-1
    dfi['BO']=dfi['BOH']+dfi['BOL']
    B=[]
    for i in dfi.index:
        if dfi['BO'].ix[i]==1:
            B.append(1) 
        elif dfi['BO'].ix[i]==-1:
            B.append(-1)
        elif len(B)==0:
            B.append(0)
        else:
            if B[-1]==0:
                B.append(0) 
            elif B[-1]==1:
                if dfi['Low'][i]<dfi['rMIN8'][i]:
                    B.append(0)
                else:B.append(1)
            elif B[-1]==-1:
                if dfi['High'][i]>dfi['rMAX8'][i]:
                    B.append(0)
                else:B.append(-1)
    dfi['sig']=B
    B=[]
    for i in dfi.index:
        if dfi['sig'].ix[i]==0:
            B.append(0)
        elif dfi['sig'].ix[i]!=0:
            if B[-1]==0:
                B.append(100/(dfi['ATR'][i]*2))
            else:
                B.append(B[-1])  
        else:
            B.append(B[-1])

    dfi['invested']=B
    dfi['pch']=dfi['Adj Close'].pct_change(periods=1)
    dfi['simple']=(dfi['pch']*dfi['sig'])+1
    dfi['lev']=(dfi['pch']*dfi['invested']*dfi['sig']*0.1)+1
    dfi['simple_pnl']=dfi['simple'].cumprod()
    dfi['lev_pnl']=dfi['lev'].cumprod()
                

    print dfi.to_string()
    plt.subplot(111)
    plt.plot(dfi.index,dfi[['simple_pnl','lev_pnl']])
    plt.show()