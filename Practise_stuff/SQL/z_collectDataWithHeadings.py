#!/usr/bin/python
# -*- coding: utf-8 -*-

import MySQLdb as mdb
import sys


con = mdb.connect('localhost', "root","MySQLoo","mydb");

with con:

    cur = con.cursor()
    cur.execute("SELECT * FROM Writers")

    rows = cur.fetchall()

    desc = cur.description

    print "%s %3s" % (desc[0][0], desc[1][0])

    for row in rows:    
        print "%2s %3s" % row