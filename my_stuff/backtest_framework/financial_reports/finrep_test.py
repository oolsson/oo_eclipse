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
# 
fin.add_many_2ax(["OFDP/FUTURE_NG1","CHRIS/CME_AD1.6"],start2,end1,title1='NAT GAS',legend1=['NZD','BR'])
# fin.add_many(["OFDP/FUTURE_NG1","CHRIS/CME_AD1.6"],start2,end1,title1='NAT GAS',legend1=['NZD','BR'])
# 
# fin.add_relative_perf(["CHRIS/CME_AD1.6",
#                        "CHRIS/CME_BR1.6"],start2,end1,title1='Relative performance',columns=['NZD','BR'])
fin.write_rep('oopoooc') 