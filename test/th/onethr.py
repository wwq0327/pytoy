#!/usr/bin/env python

from time import sleep, ctime

def loop(th, t):
    print 'start loop %s at: %s' % (th, ctime())
    sleep(t)
    print 'loop %s at: %s' % (th, ctime())

def main():
    print 'starting at:', ctime()
    loop(0, 4)
    loop(1, 2)
    print 'All DONE at:' , ctime()

if __name__ == '__main__':
    main()

