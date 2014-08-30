import pandas.rpy.common as com
import rpy2.robjects as robjects
from rpy2.robjects.packages import importr

xts = importr("xts", robject_translations = {".subset.xts": "_subset_xts2", 
                                             "to.period": "to_period2"})
d = {'skeleton_TA': 'skeleton_TA2'}
quantmod = importr("quantmod", robject_translations = d) 



#quantmod.getFinancials("IBM")
a=quantmod.getFinancials("IBM")  # automatically assigns data to "IBM.f" object   (#deesent seem to work because the IBM file doesn't end up in the R temp directory

#oo=com.load_data(quantmod.getFinancials("IBM"))
print a



#b=quantmod.viewFinancials(IBM.f,"BS","Q")
#print b