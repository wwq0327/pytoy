#!/usr/bin/env python
# -*- coding: utf-8 -*-
# wwq @ 2013-10-08 13:34:00

from threading import Thread
from Queue import Queue

queue = Queue()

def h():
    '''单件工作的函数'''
    print "Hello, world!"

def hello(i,q):
    '''组织多线程'''
    while True:
        print "Thread #%s" % i 
        h = q.get()
        h()
        q.task_done()

def run():
    '''执行函数'''
    for i in range(3):
        worker = Thread(target=hello, args=(i,queue))
        worker.setDaemon(True)
        worker.start()

    for j in range(6):
        queue.put(h)

    print "Main Thread Waiting"
    queue.join()
    print "Done!"

if __name__ == '__main__':
    run()
