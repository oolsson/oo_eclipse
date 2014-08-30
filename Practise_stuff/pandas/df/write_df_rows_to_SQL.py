import MySQLdb as mdb
import pandas.io.sql as sql
import pandas as pd
import numpy as np
randn = np.random.randn

def uniquify(df_columns):
    seen = set()

    for item in df_columns:
        fudge = 1
        newitem = item

        while newitem in seen:
            fudge += 1
            newitem = "{}_{}".format(item, fudge)

        yield newitem
        seen.add(newitem)

con = mdb.connect('localhost', "root","","test");

index = pd.date_range('1/1/2001', periods=5)
df = pd.DataFrame(randn(5, 5), index=index,columns=['A', 'B', 'C','D','A'])
df['date']=df.index

col=list(uniquify(df.columns))
print col
print df.columns
df.columns=col

print df
# table = pd.pivot_table(df,values=['A'], rows=df.columns,cols=['date'])

# table = df.transpose()
# print table


for row in df.index:
    df2=pd.DataFrame(columns=df.columns,index=[0])
    df2.ix[0]=df.ix[row]
#     print df2
    try:
        sql.write_frame(df2, con=con, name='t1', if_exists='append', flavor='mysql')
    except:pass