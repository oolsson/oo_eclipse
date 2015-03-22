import zz_my.oo_reportclss as orc
import datetime as dt
import numpy as np
import pandas as pd



start1=dt.date(1950,9,30)  
start2=dt.date(1950,1,30)      
end1=dt.date.today()

fin=orc.fin()
# fin.add_df(df,title1='NAT GAS',legend1=['NZD','BR'])
fin.add(["FRED/ISRATIO"],start1,end1,title1='inventory to sales ratio')
fin.add(["FRED/BUSINV"],start1,end1,title1='Total Business Inventories')
fin.add(["FRED/MNFCTRIRSA"],start1,end1,title1='manufactoring inv to sales')
fin.add(["FRED/COMPUTSA"],start1,end1,title1='private housing units compleated')
fin.add(["FRED/PERMIT"],start1,end1,title1='private building permits')
fin.add(["FRED/HOUST"],start1,end1,title1='private house starts')
fin.add(["FRED/PNFI"],start1,end1,title1='Private Nonresidential Fixed Investment')
fin.add(["FRED/TCU"],start1,end1,title1='capacity utilization')
fin.add_multichart(["FRED/REALLNNSA","FRED/TOTCINSA","FRED/CILDCBW027NBOG","FRED/CLSACBW027NBOG","FRED/MVLOAS","FRED/DTBOVNM"],start2,end1,(2,-1),legend1=[7,8,2,3,4,5])
fin.add(["FRED/SLOAS"],start1,end1,title1='Student Loans')
fin.add_multichart(["FRED/DRTSPM","FRED/DRTSNT","FRED/STDSAUTO","FRED/DRTSCLCC","FRED/DRTSCIS","FRED/DRTSCILM"],start2,end1,(2,-1),legend1=[7,8,2,3,4,5])
fin.add(["FRED/NEWORDER"],start1,end1,title1='Manufacturers New Orders: Nondefense Capital Goods Excluding Aircraft')
fin.add(["FRED/IBLFRIW027SBOG"],start1,end1,title1='Interbank Loans, Foreign-Related Institutions')
fin.add(["FRED/CPFF"],start1,end1,title1='3-Month Commercial Paper Minus Federal Funds Rate')
fin.add(["FRED/ICSA"],start1,end1,title1='Initial Claims')
fin.add(["FRED/TEDRATE"],start1,end1,title1='TED libor over treasurt 3m')
fin.add_multichart(["ML/AAAEY","ML/BEY","ML/AAOAS","ML/USTRI","ML/EMHGY","ML/EEMCBI"],start2,end1,(2,-1),legend1=['US AAA yield','US B yield','US AA OAS','US high yield','EM high grade','Europe EM yield'])
fin.add(["OECD/MEI_CLI_LOLITOAA_USA_M"],start1,end1,title1='US LEI')
fin.add(["OECD/SNA_TABLE4_USA_PPPGDP_CD_A"],start1,end1,title1='us ppp')


# fin.add(["OECD/SNA_TABLE4_GBR_PPPGDP_CD_A"],start1,end1,title1='x')
# fin.add(["OECD/SNA_TABLE4_ESP_PPPGDP_CD_A"],start1,end1,title1='x')
# fin.add_chart(["OFDP/FUTURE_NG1"],start1,end1,title1='NAT GAS')
# fin.add_multichart(["OFDP/FUTURE_NG1","CHRIS/CME_AD1.6","OFDP/FUTURE_NG1","OFDP/FUTURE_NG1","CHRIS/CME_AD1.6","CHRIS/CME_AD1.6"],start2,end1,(2,-1),legend1=[7,8,2,3,4,5])
# fin.add_many_2ax(["OFDP/FUTURE_NG1","CHRIS/CME_AD1.6"],start2,end1,title1='NAT GAS',legend1=['NZD','BR'])
# fin.add_many(["OFDP/FUTURE_NG1","CHRIS/CME_AD1.6"],start2,end1,title1='NAT GAS',legend1=['NZD','BR'])
# fin.add_relative_perf(["CHRIS/CME_AD1.6",
#                        "CHRIS/CME_BR1.6"],start2,end1,title1='Relative performance',columns=['NZD','BR'])


fin.write_rep('us_econ') 