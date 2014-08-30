#http://pandas.pydata.org/pandas-docs/dev/io.html
import pandas as pd
#data=pd.read_fwf

#splits a large text import into chunk sizes
rd=pd.read_csv("C:\Users\oo\Downloads\kibot\ETF\Daily\AADR.txt",parse_dates=True,index_col=0,chunksize=5,names=['open','high','low','close','vol'])
for chunk in rd:
    print chunk
print rd   
    
#imports data with     
#f1 = lambda x: float(x)
#data = pd.read_csv("C:\Users\oo\Downloads\kibot\ETF\Daily\AADR.txt",parse_dates=True,index_col=0,\
#                   names=['open','high','low','close','vol'],converters={'vol':f1})
#print help(pd.read_csv)

#print data.to_string()