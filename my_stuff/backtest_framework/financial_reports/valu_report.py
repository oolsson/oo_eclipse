import zz_my.oo_reportclss as orc
import datetime as dt
import numpy as np
import pandas as pd



start1=dt.date(2014,9,30)  
start2=dt.date(2015,1,30)   
start3=dt.date(1995,1,30)   
end1=dt.date.today()
fin=orc.fin()

 
# fin.add_crossvalue(['SPY','IWM','EWC','EWW','EWG','EWQ','EWP','EWI','EWL'
# ,'GREK','RSX','TUR','EZA','EWJ','EWH','EWI',
# 'EWY','EWA','EPI','IJH','PIN','EWS','EWM','VNM'])
# fin.add_crossvalue(['IBB','IYR','ICF','IYW','IYH','IYE','ITB','REM',
#                     'IYT','IHE','IYF','IYC','IYJ','IHF','IYK','IHI',
#                     'IYZ','IDU','IYG','ITA','IAT','IEO','IYM','SOXX',
#                     'IEZ','RES','IAI','IAK','FTY'])
fin.add_hist_value(['SPY','IWM','EWC'],start3,end1)

fin.write_rep('value') 