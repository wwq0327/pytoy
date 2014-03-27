#!/usr/bin/env python

import httplib
import threading

THREAD_COUNT = 10

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
    t = threading.currentThread()
    print t.name + 'sub thread'

    for i in range(30):
        test_performace('192.168.1.100', '/projects/13/')

def main():
    Threads = []
    for i in range(THREAD_COUNT):
        t = threading.Thread(target=test, name="T"+str(i))
        t.setDaemon(True)
        Threads.append(t)

    for t in Threads:
        t.start()

    for t in Threads:
        t.join()

if __name__ == '__main__':
    main()
