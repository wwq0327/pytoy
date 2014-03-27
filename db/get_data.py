#!/usr/bin/env python

import MySQLdb as mdb
import sys

con = mdb.connect('localhost', 'root', '123', 'testdb')

with con:
    cur = con.cursor()
    cur.execute("select * from writers")
    rows = cur.fetchall()
    for row in rows:
        print row
