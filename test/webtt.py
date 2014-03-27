#!/usr/bin/env python

import httplib

def test_performace(server, url):
    conn = httplib.HTTPConnection(server)
    try:
        conn.request('GET', url)
        rsps = conn.getresponse()
        if rsps.status == 200:
            data = rsps.read()
            test_count += 1
    except:
        pass
    conn.close()

def test():
    for i in range(200):
        test_performace('192.168.1.100', '/projects/13/')

if __name__ == '__main__':
    test()
