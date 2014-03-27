#!/usr/bin/env python

import threading, time

a = 50
b = 50
c = 50
d = 50

def printvars():
    print "a = ", a
    print "b = ", b
    print "c = ", c
    print "d = ", d

def threadcode():
    global a, b, c, d
    a += 50
    b = b + 50
    c = 100
    d = 'Hello'
    print "[ChildThread] Values of variables in child thread:"
    printvars()

if __name__ == '__main__':

    print "[Mainthread] Values of variables before child thread:"
    printvars()

    t = threading.Thread(target=threadcode, name="ChildThread")
    t.setDaemon(1)
    t.start()
    t.join()

    print "[MainThread] Variables after child thread:"
    printvars()
