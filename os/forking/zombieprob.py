#!/usr/bin/env python

import os, time

print "Before the fork, my PID is ", os.getpid()

pid = os.fork()

if pid:
    print "Hello form the parent. The child will be PID %d" % pid
    print "Sleeping 12 seconds..."
    time.sleep(12)

