#!/usr/bin/env python

import MySQLdb as mdb
import sys

con = mdb.connect('localhost', 'root', '123', 'testdb')

with con:
    cur = con.cursor()
    cur.execute("create table if not exists \
    writers(id int primary key auto_increment, name varchar(25))")
    cur.execute("insert into writers(name) values('wyatt')")
    cur.execute("insert into writers(name) values('wwq0327')")


