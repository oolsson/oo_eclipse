from pandas.io.data import DataReader
from datetime import datetime
import datetime as dt
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import zz_my.reportclss as rp
from pandas.tseries.offsets import *
import Quandl

end=dt.datetime.today()
start=datetime(1980,1,1)

rep=rp.newreport()
pic=rp.pic_num()
rep.addlogo()


f = lambda x: float(x)
 
#yieldspread model-----------------------------------------------------------------------------------------
# EQ = DataReader("SP500",  "fred", start, end) #SPX
EQ=Quandl.get("YAHOO/INDEX_GSPC.6",trim_start =start, trim_end=end, authtoken="XgkWhb4QXS6cgd4AxWSz")
LB = DataReader("DGS10",  "fred", start, end) #10y
SB = DataReader("DGS2",  "fred", start, end) #2y
YS=pd.merge(EQ, LB, how='outer', left_index=True, right_index=True)
YS=pd.merge(YS, SB, how='outer', left_index=True, right_index=True)
YS.columns=['EQ','LB','SB']
YS['EQ']=YS['EQ'].replace('.',np.nan).fillna(method='ffill')
YS['LB']=YS['LB'].replace('.',np.nan).fillna(method='ffill')
YS['SB']=YS['SB'].replace('.',np.nan).fillna(method='ffill')
US_YS=YS
US_YS[['EQ','LB','SB']]=YS[['EQ','LB','SB']].applymap(f)
US_YS['MAS']=pd.rolling_mean(US_YS['EQ'], 300)
US_YS['MAL']=pd.rolling_mean(US_YS['EQ'], 500)
US_YS['spread']=US_YS['LB']-US_YS['SB']

   
trade =list(np.zeros(500))
i=500
pos3=0
while i < len(US_YS['EQ']):
    if US_YS['EQ'].ix[i] >US_YS['MAS'].ix[i] and US_YS['spread'].ix[i]>0.75:
        pos3=1
        trade.append(pos3)
    elif US_YS['EQ'].ix[i]<US_YS['MAL'].ix[i] and min(US_YS['spread'].ix[i-500:i])<0.5:
        pos3=0
        trade.append(pos3)
    else:
        pos3 = pos3
        trade.append(pos3)
    i=i+1
   
US_YS['sig']=trade
US_YS['PNL']=US_YS['EQ'].pct_change(periods=1)*US_YS['sig']+1
US_YS['PNL']= US_YS['PNL'].cumprod()
      
print US_YS.tail(5)   
plt.subplot(411)
plt.plot(US_YS.index,US_YS[['EQ','MAS','MAL']])
plt.subplot(412)
plt.plot(US_YS.index,US_YS['spread'])
plt.subplot(413)
plt.plot(US_YS.index,US_YS['PNL'])
plt.subplot(414)
plt.fill_between(US_YS.index, US_YS['sig'].values,0)
# plt.show()
pic.new()
plt.savefig("C:/Users/oskar/Documents/doc_no_backup/python_crap/temp/%s.png" %(str(pic.num)))
rep.addimage("C:/Users/oskar/Documents/doc_no_backup/python_crap/temp/%s.png"%(str(pic.num)),7,4,'LEFT')
plt.close()
  
  
  
##unemployment model-----------------------------------------------------------------------------------------
UNEMP = DataReader("UNRATE",  "fred", start, end) #Unemplyment
N_UNEMP = DataReader("NROU",  "fred", start, end) #natural rate Unemplyment
# EQ = DataReader("SP500",  "fred", start, end) #SPX
UNEMP=pd.merge(UNEMP, N_UNEMP, how='outer', left_index=True, right_index=True)
UNEMP=pd.merge(UNEMP, EQ, how='inner', left_index=True, right_index=True)
UNEMP = UNEMP.replace('.',np.nan).fillna(method='ffill')
UNEMP.columns=['UNEMP','N_UNEMP','EQ']
UNEMP['MAS']=pd.rolling_mean(UNEMP['EQ'], 15)
UNEMP[['UNEMP','N_UNEMP','EQ']]=UNEMP[['UNEMP','N_UNEMP','EQ']].applymap(f)
UNEMP['Excess']=UNEMP['UNEMP']-UNEMP['N_UNEMP']
   
trade =list(np.zeros(15))
i=15
pos3=0
while i < len(UNEMP['EQ']):
    if UNEMP['EQ'].ix[i] >UNEMP['MAS'].ix[i] and UNEMP['Excess'].ix[i]>0.0:
        pos3=1
        trade.append(pos3)
    elif UNEMP['EQ'].ix[i] <UNEMP['MAS'].ix[i] and min(UNEMP['Excess'].ix[i-12:i])<0.0:
        pos3=0
        trade.append(pos3)
    else:
        pos3 = pos3
        trade.append(pos3)
    i=i+1
   
UNEMP['sig']=trade
UNEMP['PNL']=UNEMP['EQ'].pct_change(periods=1)*UNEMP['sig']+1
UNEMP['PNL']= UNEMP['PNL'].cumprod()

print UNEMP.tail(5)   
plt.subplot(411)
plt.plot(UNEMP.index,UNEMP[['EQ','MAS']])
plt.subplot(412)
plt.plot(UNEMP.index,UNEMP['Excess'])
plt.subplot(413)
plt.fill_between(UNEMP.index,UNEMP['sig'],0)
plt.subplot(414)
plt.plot(UNEMP.index,UNEMP['PNL'])
##plt.show()
pic.new()
plt.savefig("C:/Users/oskar/Documents/doc_no_backup/python_crap/temp/%s.png" %(str(pic.num)))
rep.addimage("C:/Users/oskar/Documents/doc_no_backup/python_crap/temp/%s.png"%(str(pic.num)),7,4,'LEFT')
plt.close()
 
# Inflation model-----------------------------------------------------------------------------------------------------------
INF = DataReader("CPIAUCSL",  "fred", start, end) #natural rate Unemplyment
# EQ = DataReader("SP500",  "fred", start, end) #SPX
# INF['EQ']=EQ['SP500']
INF['EQ']=US_YS['EQ']
INF = INF.replace('.',np.nan).fillna(method='ffill')
INF.columns=['CPI','EQ']
INF[['CPI','EQ']]=INF[['CPI','EQ']].applymap(f)
INF['CPI_ch']=INF['CPI'].pct_change(12)
INF=pd.DataFrame(INF)
INF['MAS']=pd.rolling_mean(INF['CPI_ch'], 1)
INF['MAL']=pd.rolling_mean(INF['CPI_ch'], 24)
INF['EQ_MA']=pd.rolling_mean(INF['EQ'], 12)
INF['CPI_diff']=INF['MAS']-INF['MAL']
 
trade =list(np.zeros(4))
i=4
pos3=0
crit_level=0.01

while i < len(INF['CPI_ch']):
    a=np.array([INF['CPI_diff'].ix[i] >crit_level,INF['MAS'].ix[i]>0.035,pos3==1])
    b=np.array([INF['MAS'].ix[i] <INF['MAL'].ix[i], pos3==0, INF['EQ'].ix[i]>INF['EQ_MA'].ix[i]])
    if a.all():
        pos3=0
        trade.append(pos3)
    elif b.all():
        pos3=1
        trade.append(pos3)
    else:
        pos3 = pos3
        trade.append(pos3)
    i=i+1

INF['sig']=trade
INF['PNL']=INF['EQ'].pct_change(periods=1)*INF['sig']+1
INF['PNL']= INF['PNL'].cumprod()

print INF.tail(5) 
# print INF.to_string()
plt.subplot(411)
plt.plot(INF.index,INF['EQ'])
plt.subplot(412)
plt.plot(INF.index,INF[['CPI_ch','CPI_ch','MAS','MAL']])
plt.subplot(413)
plt.fill_between(INF.index,INF['sig'],0)
plt.subplot(414)
plt.plot(INF.index,INF['PNL'])

# plt.show()
pic.new()
plt.savefig("C:/Users/oskar/Documents/doc_no_backup/python_crap/temp/%s.png" %(str(pic.num)))
rep.addimage("C:/Users/oskar/Documents/doc_no_backup/python_crap/temp/%s.png"%(str(pic.num)),7,4,'LEFT')
plt.close()
#

#corporate profits------------
C_POFIT = DataReader("CP",  "fred", start, end) #corporate profit after tax
C_POFIT['lag6m']=C_POFIT['CP'].shift(2)
C_POFIT['SIG']=C_POFIT['CP']>C_POFIT['lag6m']
C_POFIT=C_POFIT.shift(5, freq='D')
# print C_POFIT.to_string()

print C_POFIT.tail(5)    
plt.subplot(211)
plt.plot(C_POFIT.index,C_POFIT[['CP','lag6m']])
plt.subplot(212)
plt.fill_between(C_POFIT.index,C_POFIT['SIG'],0)
# plt.show()
   
pic.new()
plt.savefig("C:/Users/oskar/Documents/doc_no_backup/python_crap/temp/%s.png" %(str(pic.num)))
rep.addimage("C:/Users/oskar/Documents/doc_no_backup/python_crap/temp/%s.png"%(str(pic.num)),7,4,'LEFT')
plt.close()
##

#creating portfolio----------------------------------------------------------------------------------
portfolio=pd.DataFrame(US_YS['sig'],columns=['YS'])

df2=pd.DataFrame(UNEMP['sig'],columns=['UNEMP'])
df2=df2.asfreq('D', method='pad')
portfolio['UNEMP']=UNEMP['sig']

df2=pd.DataFrame(INF['sig'],columns=['INF'])
df2=df2.asfreq('D', method='pad')
portfolio['INF']=UNEMP['sig']

df2=pd.DataFrame(C_POFIT['SIG']*1,columns=['CP'])
# print df2.head(2000).to_string()
df2=df2.asfreq('D', method='pad')
# print df2.head(2000).to_string()
portfolio['CP']=df2['CP']

portfolio=portfolio.fillna(method='ffill')
portfolio=portfolio.fillna(method='bfill')
portfolio=portfolio/4
# print portfolio.head(1000).to_string()

#creating cum signal------------------------------------------------
portfolio['cum_sig']=portfolio.sum(axis=1, skipna=True)
portfolio['ret']=US_YS['EQ'].pct_change(periods=1)*portfolio['cum_sig']+1
portfolio['pnl'] =portfolio['ret'].cumprod()
# print portfolio.to_string()

# print portfolio.to_string()
plt.subplot(211)
plt.plot(portfolio.index,portfolio['cum_sig'])
plt.subplot(212)
plt.plot(portfolio.index,portfolio['pnl'])
# plt.show()
pic.new()
plt.savefig("C:/Users/oskar/Documents/doc_no_backup/python_crap/temp/%s.png" %(str(pic.num)))
rep.addimage("C:/Users/oskar/Documents/doc_no_backup/python_crap/temp/%s.png"%(str(pic.num)),7,4,'LEFT')
plt.close()


#creating specific signal------------------------------------------------
#portsig_str=portfolio.astype(str)
#portsig_str['C']=portsig_str['YS']+portsig_str['UNEMP']
#
#print portsig_str.to_string()

#plt.plot(portsig.index,portsig.astype(int))
#plt.plot(portsig_str.index,portsig_str.astype(int))
#plt.show()


rep.writereport('AA')
print 'pp'