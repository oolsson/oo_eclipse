#!/usr/bin/python
# -*- coding: utf-8 -*-

import MySQLdb as mdb
import sys


con = mdb.connect('localhost', "root","MySQLoo","minutedata1");

with con: 

    cur = con.cursor()
    cur.execute("SELECT * FROM aa")

    rows = cur.fetchall()
    print rows
    
    #p=rows[1]
    #print p[0]

    #for row in rows:
        #print row