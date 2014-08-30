#http://pandas.pydata.org/pandas-docs/dev/io.html
import pandas as pd
import io
import MySQLdb as mdb
import pandas.io.sql as sql
import numpy as np

#splits a large text import into chunk sizes
# rd=pd.read_csv("F:\My_kibot\Data\ETF\djusted\Intraday\GMMB.txt",parse_dates=True,index_col=0,chunksize=5,names=['open','high','low','close','vol'])
# for chunk in rd:
#     print chunk
# print rd   
    
#imports data with     
#f1 = lambda x: float(x)
con = mdb.connect('localhost', "root","","Pitrading");

# df = pd.read_csv("F:\My_kibot\Data\ETF\djusted\Intraday\GMMB.txt", parse_dates = [[0,1]], header = None, index_col = 0)
df = pd.read_csv("F:\My_kibot\Data\ETF\djusted\Intraday\GMMB.txt", parse_dates = [[0,1]], header = None)
df.columns=['dt','open','high','low','close','vol']


sql.write_frame(df, con=con, name='GMMB', 
                if_exists='append', flavor='mysql')
#if_exists: {'fail', 'replace', 'append'}, default 'fail'
#     fail: If table exists, do nothing.
#     replace: If table exists, drop it, recreate it, and insert data.
#     append: If table exists, insert data. Create if does not exist.
# print help(pd.read_csv)

print df.head(4)
