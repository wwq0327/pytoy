#!/usr/bin/env python
# -*- coding: utf-8 -*-

import MySQLdb
import sys

class Connection:
    def __init__(self, host, database, user=None, passwd=None):
        self.host = host
        self.database = database
        self.user = user
        self.passwd = passwd

        self._db = None
        self.connect()

    def connect(self):
        try:
            self._db = MySQLdb.connect(self.host, self.database, self.user, self.passwd)
        except MySQLdb.Error, e:
            print "Error %d: %s" % (e.args[0], e.args[1])
            sys.exit(1)

    def close(self):
        self._db.close()
        self._db = None



