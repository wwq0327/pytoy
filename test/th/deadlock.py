#!/usr/bin/env python
import threading, time

a = 5
alock = threading.Lock()
b = 5
block = threading.Lock()

def thread1calc():
    print "Thread1 acquiring lock a"
    alock.acquire()
    time.sleep(5)

    print "Thread1 acquiring lock b"
    block.acquire()
    time.sleep(5)
    a += 5
    b += 5

    print "Thread1 releasing both locks"
    block.release()
    alock.release()

def thread2calc():
    print "Thread2 acquiring lock b"
    block.acquire()
    time.sleep(5)

    print "Thread2 acquiring lock a"
    alock.acquire()
    time.sleep(5)
    a += 5
    b += 5

    print "Thread1 releasing both locks"
    alock.release()
    block.release()

t = threading.Thread(target=thread1calc)
t.setDaemon(1)
t.start()

t = threading.Thread(target=thread2calc)
t.setDaemon(2)
t.start()

while 1:
    time.sleep(300)

