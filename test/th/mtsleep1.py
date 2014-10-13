#!/usr/bin/env python

import thread
from time import sleep, ctime

def loop(th, t):
    print 'start loop %s at: %s' % (th, ctime())
    sleep(t)
    print 'loop %s at: %s' % (th, ctime())

def main():
    print 'starting at:', ctime()
    thread.start_new_thread(loop, (0, 4))
    thread.start_new_thread(loop, (1, 2))
    sleep(6)
    print 'All DONE at:' , ctime()

if __name__ == '__main__':
    main()

