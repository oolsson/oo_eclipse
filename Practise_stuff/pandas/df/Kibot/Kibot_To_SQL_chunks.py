#http://pandas.pydata.org/pandas-docs/dev/io.html
import pandas as pd
import io
import MySQLdb as mdb
import pandas.io.sql as sql
import numpy as np
import time

con = mdb.connect('localhost', "root","","Pitrading");

# splits a large text import into chunk sizes

t0 = time.clock()
i=1
rd=pd.read_csv("F:\My_kibot\Data\ETF\djusted\Intraday\GLD.txt",parse_dates=[[0,1]],header = None,chunksize=10000)
for chunk in rd:
    chunk.columns=['dt','open','high','low','close','vol']
    sql.write_frame(chunk, con=con, name='GLD', if_exists='append', flavor='mysql')
    print i
    i +=1
    print time.clock() - t0, "seconds process time"
print rd 

    





# sql.write_frame(df, con=con, name='GMMB', 
#                 if_exists='append', flavor='mysql')
#if_exists: {'fail', 'replace', 'append'}, default 'fail'
#     fail: If table exists, do nothing.
#     replace: If table exists, drop it, recreate it, and insert data.
#     append: If table exists, insert data. Create if does not exist.
# print help(pd.read_csv)

