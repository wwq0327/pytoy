#!/usr/bin/env python

import httplib
import threading

THREAD_COUNT = 2

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

def do(server, url):
    t = threading.currentThread()
    print t.name + 'sub thread'

    for i in range(10):
        test_performace(server, url)

def main():
    Threads = []
    for i in range(THREAD_COUNT):
        t = threading.Thread(target=do, args=('192.168.1.100', '/'), name="T"+str(i))
        t.setDaemon(True)
        Threads.append(t)

    for t in Threads:
        t.start()

    for t in Threads:
        t.join()

if __name__ == '__main__':
    main()
