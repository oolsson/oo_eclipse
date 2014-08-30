

import MySQLdb
import sys

try:
    db = MySQLdb.connect(host = 'localhost', user = 'root', passwd = '', db = 'test')
    
except Exception as e:
    sys.exit('we cant get into the database')
    
    
cursor = db.cursor
print cursor
cursor.execute('select * from t1')
#print dir(cursor)

#result = cursor.fetchall()
#print result