#http://pandas.pydata.org/pandas-docs/dev/io.html
import pandas 
data = pandas.read_csv("C:\Users\oo\Documents\python_none_pythonfiles\excel\hist_EURIBOR_2012.csv",parse_dates=True)
print data.to_string()