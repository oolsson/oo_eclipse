import pandas as pd
import numpy as np
from pandas.io.parsers import *


xl = pd.ExcelFile("C:\Users\oskar\Documents\GitHub\oo_eclipse\my_stuff\Data\Retail_turnover.xls")
x = xl.parse("Sheet1")
