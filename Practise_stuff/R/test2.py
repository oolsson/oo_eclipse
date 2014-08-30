
import rpy2.robjects as robjects
from rpy2.robjects.packages import importr
util = importr("quantmod")


a=r.getFinancials("IBM")  # automatically assigns data to "IBM.f" object
r.viewFinancials(IBM.f,"BS","Q")  # quarterly balance sheet
raw_input()