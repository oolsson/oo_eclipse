#http://pandas.pydata.org/pandas-docs/dev/io.html
import datetime as dt
import pandas as pd
from pandas.io.data import DataReader
import numpy as np
data = DataReader('GooG', "yahoo", '2013-02-02','2013-03-02')
print data
data.to_csv("C:\Users\oskar\Documents\doc_no_backup\python_crap\excel\deol.csv")
lastline = raw_input(">")
