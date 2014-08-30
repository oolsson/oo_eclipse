#!/usr/bin/python
# -*- coding: utf-8 -*-

import MySQLdb as mdb
import sys

con = mdb.connect('localhost', "root","","test");

with con:
    cur = con.cursor(mdb.cursors.DictCursor)
    cur.execute("SELECT COLUMN_NAME FROM information_schema.columns WHERE  table_name = 't1' ORDER  BY ordinal_position")
    rows = cur.fetchall()
    print rows
    list1=[]
    for row in rows:
        list1.append(row["COLUMN_NAME"])
print list1