#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 共享变量，数据在线程中共享。
import threading, time

a, b, c, d =  50, 50, 50, 50

def printvars():
    print 'a =', a
    print 'b =', b
    print 'c =', c
    print 'd =', d

def threadcode():
    global a, b, c, d
    a += 50
    b = b + 50
    c = 100
    d = "Hello"
    print "[childThread] Values of variables in child thread:"
    printvars()
print "[MainThread] Values of variables in child thread:"
printvars()

# Create new thread
t = threading.Thread(target=threadcode, name="ChildThread")

# This thread won't keep the program from terminating.
t.setDaemon(1)

t.start()
t.join()

print "[MainThread] Values of variables in child thread:"
printvars()
