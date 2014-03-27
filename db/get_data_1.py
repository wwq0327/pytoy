#!/usr/bin/env python

import MySQLdb as mdb
import sys

con = mdb.connect('localhost', 'root', '123', 'testdb')

with con:
    cur = con.cursor()
    cur.execute("select * from writers")
    numrows = int(cur.rowcount)

    for i in range(numrows):
        row = cur.fetchone()
        print row[0], row[1]
