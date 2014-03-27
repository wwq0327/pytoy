#!/usr/bin/env python

import os, time, signal

def chldhandler(signum, stackframe):
    while 1:
        try:
            result = os.waitpid(-1, os.WNOHANG)
        except:
            break

        print "Reaped child process %d" % result[0]
    signal.signal(signal.SIGCHLD, chldhandler)

signal.signal(signal.SIGCHLD, chldhandler)

print "Before the fork, my PID is ", os.getpid()

pid = os.fork()
if pid:
    print "Hello from the parent. The child will be PID %d" % pid
    print "Sleeping 10 seconds..."
    time.sleep(10)
    print "Sleep done."
else:
    print "Child sleeping 5 seconds..."
    time.sleep(5)

