import pandas as pd
from pandas.io.data import DataReader
import datetime as dt
import MySQLdb as mdb
import pandas.io.sql as sql

# df1=pd.DataFrame([1,1,1,1,1,0,0,1,1],index=['a','b','c','d','e','g','h','i','j'],columns=['sig'])
# df2=pd.DataFrame([0,0,100,100,100,1,1,1],index=['a','b','c','d','e','f','g','h'],columns=['holdings'])

        #from here below is the same as in the beginning og gui, could be turned into a function   # this part needs to go in to the loop
SQL_con = mdb.connect('localhost', "root","","test");
sqll="SELECT * FROM Magic_pos"
df=sql.read_frame(sqll, SQL_con)
SQL_con.close()
df.index =  df.iloc[:,1]
# df1=df.iloc[:,0]
df1=df
# print df

SQL_con = mdb.connect('localhost', "root","","test2");
sqll="SELECT * FROM holdings"
df2=sql.read_frame(sqll, SQL_con)
SQL_con.close()
df2.index=df2['ticker']
df2=df2[['holdings','ticker']]
# print df2


port= pd.merge(df1, df2, how='outer', left_index=True, right_index=True)
port=port.iloc[:,[0,2]]
port.columns=['sig','holdings']
print port
for i in port.index:
    if port['sig'][i]>0 and port['holdings'][i]>0:
        print i,'do nothing'
    elif port['sig'][i]>0:
        print 'BUY'
    elif port['holdings'][i]>0:
        print 'Sell'