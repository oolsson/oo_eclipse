import pandas as pd
import MySQLdb as mdb
import pandas.io.sql as sql
import numpy as np

df = pd.read_csv("C:\Users\oo\Documents\AA.csv")
df=df.replace(np.nan,0)

cc=list(df.columns.values)
oo=0
for i in cc:
    cc[oo]=cc[oo].replace('%','PCH')
    oo +=1
df.columns=cc



con = mdb.connect('localhost', "root","MySQLoo","fundamentals");
sql.write_frame(df, con=con, name='dd', 
                if_exists='replace', flavor='mysql')
#if_exists: {'fail', 'replace', 'append'}, default 'fail'
#     fail: If table exists, do nothing.
#     replace: If table exists, drop it, recreate it, and insert data.
#     append: If table exists, insert data. Create if does not exist.