import zz_my.oo_reportclss as orc
import datetime as dt
import numpy as np
import pandas as pd



start1=dt.date(2014,9,30)  
start2=dt.date(2015,1,30)      
end1=dt.date.today()
fin=orc.fin()

df=pd.DataFrame(np.random.randn(22,2))
print df
# fin.add_df(df,title1='NAT GAS',legend1=['NZD','BR'])

# fin.add_chart(["OFDP/FUTURE_NG1"],start1,end1,title1='NAT GAS')
# fin.add_multichart(["OFDP/FUTURE_NG1","CHRIS/CME_AD1.6","OFDP/FUTURE_NG1","OFDP/FUTURE_NG1","CHRIS/CME_AD1.6","CHRIS/CME_AD1.6"],start2,end1,(2,-1),legend1=[7,8,2,3,4,5])
# fin.add_many_2ax(["OFDP/FUTURE_NG1","CHRIS/CME_AD1.6"],start2,end1,title1='NAT GAS',legend1=['NZD','BR'])
# fin.add_many(["OFDP/FUTURE_NG1","CHRIS/CME_AD1.6"],start2,end1,title1='NAT GAS',legend1=['NZD','BR'])
fin.add_many(["USTREASURY/YIELD.1","USTREASURY/YIELD.4","USTREASURY/YIELD.6","USTREASURY/YIELD.7","USTREASURY/YIELD.9"],start2,end1,title1='us yield',legend1=['1m','1y','3y','5y','7y','10y'])
# 
# fin.add_relative_perf(["CHRIS/CME_AD1.6",
#                        "CHRIS/CME_BR1.6"],start2,end1,title1='Relative performance',columns=['NZD','BR'])
fin.write_rep('oopoooc') 