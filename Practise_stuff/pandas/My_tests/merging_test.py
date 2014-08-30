import pandas.io.sql as sql
import MySQLdb as mdb
import pandas as pd
from pandas.io.data import DataReader


con = mdb.connect('localhost', "root","","test");
sqll="SELECT * FROM Magic_pos"
df=sql.read_frame(sqll, con)
df.index=df['ticker']

con.close()
print df

con = mdb.connect('localhost', "root","","test2");
sqll="SELECT ticker,quantity FROM model_positions"
df_holdings=sql.read_frame(sqll, con)
df_holdings.index=df_holdings['ticker']
print df_holdings


port= pd.merge(df, df_holdings, how='outer', left_index=True, right_index=True)
# port=port.asfreq('D', method='pad')
# port['conc']=pd.concat(port['A'],port['B'])
print port